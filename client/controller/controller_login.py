import json
import threading

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QDialog

from client.controller.controller_common import CommonController
from client.controller.controller_membership import MembershipController
from client.view.view_login import Ui_Form as LoginView
from client.storage.temporary_storage import TemporaryStorage


class LoginController(QDialog, LoginView, CommonController, TemporaryStorage):
    def __init__(self):
        super().__init__()
        self.init_setting()
        self.init_variable()
        self.init_widget()
        self.init_signal()
        self.init_method()

    def init_setting(self):
        """
        생성자 설정
        """
        self.setupUi(self)

    def init_widget(self):
        """
        생성자 위젯 설정
        """
        # 로고 이미지
        self.lb_logo.setPixmap(QPixmap("../img/logo/logo.png"))
        self.lb_logo.setScaledContents(True)
        self.lb_logo.setFixedSize(125, 125)

        # 아이디
        self.le_id.setPlaceholderText("아이디")
        self.le_id.setEchoMode(QLineEdit.EchoMode.Normal)

        # 비밀번호
        self.le_pw.setPlaceholderText("비밀번호")
        self.le_pw.setEchoMode(QLineEdit.EchoMode.Password)

        # 로그인 버튼
        self.pb_login.setDisabled(True)

    def init_variable(self):
        """
        생성자 변수 선언 및 초기화
        """
        self.is_ok = False
        self.client_socket = self.info['socket'][0]
        self.stop_flag = False
        self.dlg = MembershipController()

    def init_signal(self):
        """
        생성자 시그널
        """
        self.le_id.textChanged.connect(self.input_id)
        self.le_pw.textChanged.connect(self.input_pw)
        self.pb_login.clicked.connect(self.process_login)
        self.pb_member.clicked.connect(self.show_membership_view)

    def init_method(self):
        """
        생성자 함수
        """
        self.only_alpha_int(self.le_id)
        self.only_alpha_int(self.le_pw)
        self.listeningThread = threading.Thread(target=self.check_server_response, daemon=True)
        self.listeningThread.start()

    def input_id(self, id: str):
        """
        로그인 버튼 비활성화 해제
        :param id: 아이디
        """
        self.id_ = id
        if self.le_pw.text() != '':
            self.pb_login.setDisabled(False)

    def input_pw(self, pw: str):
        """
        로그인 버튼 비활성화 해제
        :param pw: 비밀번호
        """
        self.pw_ = pw
        if self.le_id.text() != '':
            self.pb_login.setDisabled(False)

    def show_membership_view(self):
        self.dlg.img_path = '../img/profile/who.png'
        imgdata = open(self.dlg.img_path, 'rb').read()
        pixmap = self.dlg.mask_image(imgdata)
        self.dlg.lb_profile_img.setPixmap(pixmap)
        self.dlg.le_id.clear()
        self.dlg.le_pw.clear()
        self.dlg.le_nick.clear()
        self.dlg.lb_warning_id.clear()
        self.dlg.lb_warning_pw.clear()
        self.dlg.lb_warning_nick.clear()
        self.dlg.exec()

    def process_login(self):
        if self.info['connect'][0]:
            dict_data = {'id': self.id_, 'pw': self.pw_}
            json_data = json.dumps(dict_data)
            msg = f'login{self.header_split}{json_data}'
            self._send_json_packet(msg)

    def _send_packet(self, p):
        print(p)
        self.info['socket'][0].send(p.encode())

    def _send_json_packet(self, msg):
        print(msg)
        if self.info['connect']:
            self.client_socket.send(bytes(msg, 'utf-8'))

    def check_server_response(self):
        while not self.stop_flag:
            if not self.client_socket == None:
                try:
                    response = self.client_socket.recv(4096).decode("UTF-8")
                    self._parse_packet(response)
                except Exception as e:
                    print(e)
                    pass

    def _parse_packet(self, p: str):
        parsed = p.split(self.header_split)
        command = parsed[0]
        print('로그인' + p)
        if command == 'wrongpw':
            msg = '패스워드가 일치하지 않습니다!'
            self.lb_warning.setText(msg)
            self.lb_warning.setStyleSheet('color: red;')
        elif command == 'noneid':
            msg = '아이디가 일치하지 않습니다!'
            self.lb_warning.setText(msg)
            self.lb_warning.setStyleSheet('color: red;')
        elif command == 'login':
            self.is_ok = True
            self.info['id'] = [self.id_]
            self.info['name'] = [';'.join(parsed[1:]).strip()]
            self.close()
        elif command == 'doublenick':
            msg = '닉네임이 중복됩니다.'
            self.dlg.lb_warning_id.setText(msg)
        elif command == 'doubleid':
            msg = '해당아이디가 존재합니다.'
            self.dlg.lb_warning_nick.setText(msg)
        elif command == 'welcome':
            print('여기 탐?')
            self.dlg.close()

    def closeEvent(self, e):
        self.stop_flag = True
        self._send_packet(f'disconnect{self.header_split}')
