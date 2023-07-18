import json
import shutil
from tkinter import filedialog

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QPainter, QWindow, QBrush, QImage
from PyQt5.QtWidgets import QLineEdit, QDialog

from client.controller.controller_common import CommonController
from client.storage.temporary_storage import TemporaryStorage
from client.view.view_membership import Ui_Dialog as MembershipView


class MembershipController(QDialog, MembershipView, CommonController, TemporaryStorage):
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
        # 프로필 사진
        self.lb_profile_img.setFixedSize(150, 150)
        self.img_path = '../img/profile/who.png'
        imgdata = open(self.img_path, 'rb').read()
        pixmap = self.mask_image(imgdata)
        self.lb_profile_img.setPixmap(pixmap)
        self.lb_profile_img.setScaledContents(True)
        self.lb_profile_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 아이디
        self.le_id.setPlaceholderText("아이디")
        self.le_id.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lb_warning_id.setStyleSheet('color: red')

        # 비밀번호
        self.le_pw.setPlaceholderText("비밀번호")
        self.le_pw.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lb_warning_pw.setStyleSheet('color: red')

        # 닉네입
        self.le_nick.setPlaceholderText("닉네임")
        self.le_nick.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lb_warning_nick.setStyleSheet('color: red')

        # 회원가입 버튼
        self.pb_join.setDisabled(True)

    def init_variable(self):
        """
        생성자 변수 선언 및 초기화
        """
        # 회원가입 조건 충족 여부
        self.is_ok = False
        self.dict_info = {
            'id': '',
            'pw': '',
            'nick': '',
            'manager': '',
            'img_path': ''
        }
        self.client_socket = self.info['socket'][0]
        # self.stop_flag = False
        # self.listeningThread = threading.Thread(target=self.check_server_response, daemon=True)

    def init_signal(self):
        """
        생성자 시그널
        """
        self.pb_regist_img.clicked.connect(self.open_file)

        self.le_id.textChanged.connect(self.input_id)
        self.le_pw.textChanged.connect(self.input_pw)
        self.le_nick.textChanged.connect(self.input_nick)

        self.le_id.editingFinished.connect(self.check_id)
        self.le_pw.editingFinished.connect(self.checkPw)
        self.le_nick.editingFinished.connect(self.check_nick)

        self.pb_join.clicked.connect(self.excute_join)

    def init_method(self):
        """
        생성자 함수
        """
        self.only_smallalpha_int(self.le_id)
        self.only_alpha_int(self.le_pw)
        self.only_alpha_hangul_int(self.le_nick)

    def open_file(self):
        """
        파일 불러오기 창
        :return:
        """
        try:
            img_path = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
                ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
            file_name = img_path.split('/')[-1]
            file_path = f'../img/profile/{file_name}'
            self.move_image_file(img_path, file_path)
            self.img_path = file_path
            imgdata = open(self.img_path, 'rb').read()
            pixmap = self.mask_image(imgdata)
            self.lb_profile_img.setPixmap(pixmap)
            self.lb_profile_img.setScaledContents(True)
            self.lb_profile_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        except:
            pass

    def move_image_file(self, source_path, destination_path):
        try:
            shutil.move(source_path, destination_path)
            print("이미지 파일이 성공적으로 이동되었습니다.")
        except FileNotFoundError:
            print("소스 경로에 해당하는 이미지 파일을 찾을 수 없습니다.")
        except Exception as e:
            self.img_path = '../img/profile/who.png'
            pass

    def mask_image(self, imgdata, imgtype='png', size=64):
        """
        동그란 형태의 이미지 만들기
        :param imgtype:
        :param size:
        :return:
        """
        image = QImage.fromData(imgdata, imgtype)
        image.convertToFormat(QImage.Format_ARGB32)
        imgsize = min(image.width(), image.height())
        rect = QRect(
            (image.width() - imgsize) // 2,
            (image.height() - imgsize) // 2,
            imgsize,
            imgsize
        )
        image = image.copy(rect)

        out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
        out_img.fill(Qt.transparent)

        brush = QBrush(image)

        painter = QPainter(out_img)
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, imgsize, imgsize)
        painter.end()

        pr = QWindow().devicePixelRatio()
        pm = QPixmap.fromImage(out_img)
        pm.setDevicePixelRatio(pr)
        size *= pr
        print(size)
        pm = pm.scaled(int(size), int(size), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return pm

    def input_id(self, id: str):
        """
        회원가입 버튼 비활성화 해제
        :param id: 아이디
        """
        self.id_ = id
        self.btn_set_enable(self.is_ok, self.pb_join)

    def input_pw(self, pw: str):
        """
        회원가입 버튼 비활성화 해제
        :param pw: 비밀번호
        """
        self.pw_ = pw
        self.btn_set_enable(self.is_ok, self.pb_join)

    def input_nick(self, nick: str):
        """
        회원가입 요건 충족 시 회원가입 버튼 비활성화 해제        """
        self.nick = nick
        self.btn_set_enable(self.is_ok, self.pb_join)

    def check_id(self):
        """
        아이디 유효성 검사
        :param col: 컬럼값
        :return:
        """
        if 5 > len(self.id_) or len(self.id_) > 10:
            print(self.id_)
            msg = '최소 5자리, 최대 10자리까지 입력해주세요.'
            self.lb_warning_id.setText(msg)
            self.is_ok = False
        else:
            msg = '유효한 아이디입니다.'
            self.lb_warning_id.setText(msg)
            self.lb_warning_id.setStyleSheet('color: black;')
            self.is_ok = True

    def checkPw(self):
        """
        비밀번호 유효성 검사
        :return:
        """
        upp_cnt = 0
        low_cnt = 0
        digit_cnt = 0

        for i in self.pw_:
            if i.isupper():
                upp_cnt += 1
            if i.islower():
                low_cnt += 1
            if i.isdigit():
                digit_cnt += 1

        if self.id_ == self.pw_:
            msg = '아이디와 비밀번호를 다르게 입력해주세요.'
            self.lb_warning_pw.setText(msg)
            self.is_ok = False
        elif 8 > len(self.pw_) or len(self.pw_) > 15:
            msg = '최소 8자리, 최대 15자리까지 입력해주세요.'
            self.lb_warning_pw.setText(msg)
            self.is_ok = False
        elif upp_cnt < 1 or low_cnt < 1 or digit_cnt < 1:
            msg = '대문자, 소문자, 숫자를 최소 1개 이상 입력해주세요.'
            self.lb_warning_pw.setText(msg)
            self.is_ok = False
        else:
            msg = '유효한 비밀번호입니다.'
            self.lb_warning_pw.setText(msg)
            self.lb_warning_pw.setStyleSheet('color: black;')
            self.is_ok = True

    def check_nick(self):
        """
        닉네임 유효성 검사
        :return:
        """
        if 2 <= len(self.nick) <= 15:
            msg = '유효한 닉네임입니다.'
            self.lb_warning_nick.setText(msg)
            self.lb_warning_nick.setStyleSheet('color: black;')
            self.is_ok = True
        else:
            msg = '최소 2자리, 최대 15자리까지 입력해주세요.'
            self.lb_warning_nick.setText(msg)
            self.is_ok = False

    def excute_join(self):
        """
        회원가입 진행
        :return:
        """
        if self.is_ok:
            self.dict_info['id'] = self.id_
            self.dict_info['pw'] = self.pw_
            self.dict_info['nick'] = self.nick
            self.dict_info['manager'] = '0'
            try:
                self.dict_info['img_path'] = self.img_path
            except:
                self.dict_info['img_path'] = ''

            json_data = json.dumps(self.dict_info)
            msg = f'join{self.header_split}{json_data}'
            self._send_json_packet(msg)
        else:
            pass

    def _send_json_packet(self, msg):
        """
        제이슨 데이터 보내기
        :param msg: 제이슨 구조
        :return:
        """
        print(msg)
        if self.info['connect']:
            self.client_socket.send(bytes(msg, 'UTF-8'))
