import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog

from client.controller.controller_common import CommonController
from client.storage.temporary_storage import TemporaryStorage
from client.view.view_take import Ui_Dialog as TakeView


class TakeDialog(QDialog, TakeView, CommonController, TemporaryStorage):
    def __init__(self, code):
        super().__init__()
        self.init_setting()
        self.init_variable(code)
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

    def init_variable(self, code):
        """
        생성자 변수 선언 및 초기화
        """
        self.is_check = False
        self.code = code

    def init_widget(self):
        """
        생성자 위젯 설정
        """
        self.lb_code.setText(f"상품코드: {self.code}")

    def init_signal(self):
        """
        생성자 시그널
        """
        self.pb_check.clicked.connect(self.check_to_true)

    def init_method(self):
        """
        생성자 함수
        """

    def check_to_true(self):
        self.is_check = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = TakeDialog()
    a.exec()
    sys.exit(app.exec_())
