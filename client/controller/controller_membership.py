import json
import shutil
import sys
from datetime import datetime
from tkinter import filedialog

import bcrypt as bcrypt
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QPainter, QWindow, QBrush, QImage, QPalette, QColor
from PyQt5.QtWidgets import QLineEdit, QDialog, QListWidgetItem, QApplication

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
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

    def init_variable(self):
        """
        생성자 변수 선언 및 초기화
        """
        # 회원가입 조건 충족 여부
        self.is_ok = False

    def init_widget(self):
        """
        생성자 위젯 설정
        """
        # 프로필 사진
        self.lb_profile_img.setFixedSize(150, 150)
        self.img_path = '../img/profile/who.png'
        pixmap = QPixmap(self.img_path)
        self.lb_profile_img.setPixmap(pixmap)
        self.lb_profile_img.setScaledContents(True)
        self.lb_profile_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 아이디
        self.le_id.setEchoMode(QLineEdit.EchoMode.Normal)

        # 비밀번호
        self.le_pw.setEchoMode(QLineEdit.EchoMode.Password)

        # 이름
        self.le_name.setEchoMode(QLineEdit.EchoMode.Normal)

        # 부서
        self.le_depart.setPlaceholderText('부서')
        self.le_depart.setEchoMode(QLineEdit.EchoMode.Normal)

        # 직책
        self.le_position.setPlaceholderText('직책')
        self.le_position.setEchoMode(QLineEdit.EchoMode.Normal)

        # 경고메시지
        self.lw_msg.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.lw_msg.setStyleSheet("""
        #                     QListWidget::item {color:red;
        #                     background-color:transparent;}
        #                     """)

        # 회원가입 버튼
        self.pb_join.setDisabled(True)

    def init_signal(self):
        """
        생성자 시그널
        """
        self.pb_regist_img.clicked.connect(self.open_file)

        self.le_id.textChanged.connect(self.input_id)
        self.le_pw.textChanged.connect(self.input_pw)
        self.le_name.textChanged.connect(self.input_name)
        self.le_depart.textChanged.connect(self.input_depart)
        self.le_position.textChanged.connect(self.input_position)

        self.le_id.editingFinished.connect(self.check_id)
        self.le_pw.editingFinished.connect(self.checkPw)

        self.pb_join.clicked.connect(self.excute_join)

    def init_method(self):
        """
        생성자 함수
        """
        self.only_smallalpha_int(self.le_id)
        self.only_alpha_int(self.le_pw)
        self.only_alpha_hangul_int(self.le_name)

    def open_file(self):
        """
        파일 불러오기 창
        :return:
        """
        try:
            img_path = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
                ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
            file_name = img_path.split('/')[-1]
            file_path = f'../client/img/{file_name}'
            self.move_image_file(img_path, file_path)
            self.img_path = file_path
            pixmap = QPixmap(self.img_path)
            self.lb_profile_img.setPixmap(pixmap)
            self.lb_profile_img.setScaledContents(True)
            self.lb_profile_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        except:
            pass

    def move_image_file(self, source_path, destination_path):
        """
        파일 이동
        :param source_path: 이동 전 경로
        :param destination_path: 이동 할 경로
        :return:
        """
        try:
            shutil.move(source_path, destination_path)
            print("이미지 파일이 성공적으로 이동되었습니다.")
        except FileNotFoundError:
            print("소스 경로에 해당하는 이미지 파일을 찾을 수 없습니다.")
        except Exception as e:
            self.img_path = '../img/profile/who.png'
            pass

    def input_id(self, id: str):
        """
        아이디 담기
        :param id: 아이디
        """
        self.id_ = id
        self.btn_set_enable(self.is_ok, self.pb_join)

    def input_pw(self, pw: str):
        """
        비밀번호 담기
        :param pw: 비밀번호
        """
        self.pw_ = pw
        self.btn_set_enable(self.is_ok, self.pb_join)

    def input_name(self, name: str):
        """
        이름 담기
        :param name:
        :return:
        """
        self.name = name
        self.btn_set_enable(self.is_ok, self.pb_join)

    def input_depart(self, depart: str):
        """
        부서 담기
        :param depart:
        :return:
        """
        self.depart = depart
        self.btn_set_enable(self.is_ok, self.pb_join)

    def input_position(self, position: str):
        """
        직책 담기
        :param position:
        :return:
        """
        self.position = position
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
            self.show_warning_msg(msg)
            self.is_ok = False
        else:
            msg = '유효한 아이디입니다.'
            self.show_warning_msg(msg)
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

        if 8 > len(self.pw_) or len(self.pw_) > 15:
            msg = '최소 8자리, 최대 15자리까지 입력해주세요.'
            self.show_warning_msg(msg)
            self.is_ok = False
        elif upp_cnt < 1 or low_cnt < 1 or digit_cnt < 1:
            msg = '대문자, 소문자, 숫자를 최소 1개 이상 입력해주세요.'
            self.show_warning_msg(msg)
            self.is_ok = False
        else:
            msg = '유효한 비밀번호입니다.'
            self.show_warning_msg(msg)
            self.is_ok = True

    def show_warning_msg(self, msg):
        item = QListWidgetItem(msg)
        item.setForeground(QColor(255, 0, 0))
        # item.setBackground(QColor(0, 0, 0, 0))
        self.lw_msg.addItem(item)
        last_row_index = self.lw_msg.count() - 1
        self.lw_msg.setCurrentRow(last_row_index)

    def excute_join(self):
        """
        회원가입 진행
        :return:
        """
        self.dict_info = dict()
        if self.is_ok:
            # # 이미지 전송
            # with open(self.img_path, 'rb') as image_file:
            #     image_data = image_file.read()
            #
            # self.info['socket'][0].sendall(image_data)
            # self.send_packet(f'image{self.header_split}')

            pw = self.hash_password(self.pw_)

            print(str(pw))

            self.dict_info['id'] = [self.id_]
            self.dict_info['pw'] = [self.pw_]
            self.dict_info['name'] = [self.name]
            self.dict_info['depart'] = [self.depart]
            self.dict_info['position'] = [self.position]
            try:
                self.dict_info['img'] = [self.img_path]
            except:
                self.dict_info['img'] = ['../profile/who.png']
            self.dict_info['date'] = [datetime.now().strftime('%Y-%m-%d')]
            json_data = json.dumps(self.dict_info)
            msg = f'join{self.header_split}{json_data}'
            self.send_json_packet(msg)
        else:
            pass

    def hash_password(self, pw):
        """
        비밀번호 해시화
        :param pw: 비밀번호
        :return:
        """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(pw.encode('utf-8'), salt)
        return hashed_password


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = MembershipController()
    a.show()
    sys.exit(app.exec_())
