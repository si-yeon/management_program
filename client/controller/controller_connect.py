import sys
import threading
from socket import *

from PyQt5.QtWidgets import QApplication, QDialog

from client.controller.controller_check import CheckDialog
from client.view.view_connect import Ui_Dialog as ConnectView
from client.storage.temporary_storage import TemporaryStorage


class ConnectController(QDialog, ConnectView, TemporaryStorage):
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
        self.client_socket = None
        self.connected = False
        self.stop_flag = True

    def init_widget(self):
        """
        생성자 위젯 설정
        """

    def init_signal(self):
        """
        생성자 시그널
        """
        self.pb_connect.clicked.connect(self.connect)

    def init_method(self):
        """
        생성자 함수
        """

    def connect(self):
        """
        서버에 연결 요청
        :return:
        """
        msg = ''
        if self.pb_connect.text() == "연결":
            serverIP = self.le_ip.text()
            serverPort = self.le_port.text()  # ports 0-1024 are reserved
            self.client_socket = socket(AF_INET, SOCK_STREAM)  # SOCK_STREAM stands for TCP protocol
            try:
                self.client_socket.connect((serverIP, int(serverPort)))
                # self.pb_connect.setText('연결해제')
                self.listeningThread = threading.Thread(target=self.check_server_response, daemon=True)
                self.listeningThread.start()
                self.connected = True
                self.stop_flag = True
                self.info['socket'] = [self.client_socket]
                self.info['connect'] = [self.connected]
                msg = "연결 성공!"
            except:
                self.connected = False
                msg = "연결 불가!"
        elif self.pb_connect.text() == "연결해제":
            try:
                self.send_packet(f'disconnect{self.header_split}')
                # self.pb_connect.setText('연결')
                self.client_socket.close()
                self.connected = False
                msg = "연결 해제!"
            except Exception as e:
                self.connected = False
                msg = "연결 실패!"

        if msg != '':
            dlg = CheckDialog(msg)
            dlg.exec()
            if self.connected:
                self.close()

    def check_server_response(self):
        """
        서버 응답 체크
        :return:
        """
        while not self.stop_flag:
            if self.client_socket is not None:
                try:
                    response = self.client_socket.recv(4096).decode("UTF-8")
                    self._parse_packet(response)
                except:
                    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = ConnectController()
    a.show()
    sys.exit(app.exec_())
