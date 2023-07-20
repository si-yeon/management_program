from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from client.controller.controller_common import CommonController as Common
from client.view.view_check import Ui_Dialog as check_view


class CheckDialog(QDialog, check_view, Common):
    def __init__(self, msg):
        super().__init__()
        self.init_setting()
        self.init_variable(msg)
        self.init_widget()
        self.init_signal()

    def init_setting(self):
        """
        생성자 설정
        """
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

    def init_variable(self, msg: str):
        """
        생성자 변수 선언 및 초기화
        """
        self.is_check = False
        self.msg = msg

    def init_widget(self):
        """
        생성자 위젯 설정
        """
        self.lb_msg.setText(self.msg)

    def init_signal(self):
        """
        생성자 시그널 설정
        """
        self.pb_check.clicked.connect(self.check_to_true)

    def check_to_true(self):
        self.is_check = True
