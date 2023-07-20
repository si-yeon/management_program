from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from client.controller.controller_common import CommonController as Common
from client.view.view_name import Ui_Dialog as name_view

class NameDialog(QDialog, name_view, Common):
    def __init__(self):
        super().__init__()
        self.init_setting()
        self.init_variable()
        self.init_widget()
        self.init_signal()

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
        self.is_check = False
        self.file_name = 'excel'

    def init_widget(self):
        """
        생성자 위젯 설정
        """
        self.pb_check.setDisabled(True)

    def init_signal(self):
        """
        생성자 시그널 설정
        """
        self.pb_check.clicked.connect(self.check_to_true)
        self.le_file_name.textEdited.connect(self.input_file_name)

    def check_to_true(self):
        self.is_check = True

    def input_file_name(self, txt):
        self.file_name = txt
        self.pb_check.setDisabled(False)
