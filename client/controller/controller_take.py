import sys
import threading

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow

from client.view.view_take import Ui_Dialog as TakeView
from client.storage.temporary_storage import TemporaryStorage

class NumberController(QDialog, TakeView, TemporaryStorage):
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
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)

    def init_variable(self):
        """
        생성자 변수 선언 및 초기화
        """
        self.client_socket = self.info['socket'][0]
        self._connected = self.info['connect'][0]

    def init_widget(self):
        """
        생성자 위젯 설정
        """

    def init_signal(self):
        """
        생성자 시그널
        """

    def init_method(self):
        """
        생성자 함수
        """

    def closeEvent(self, e):
        self.close()
        self._send_packet(f'disconnect{self.header_split}')

    def _send_packet(self, p):
        self.client_socket.send(p.encode())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = NumberController()
    a.exec()
    sys.exit(app.exec_())
