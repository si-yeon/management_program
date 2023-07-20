import shutil
from tkinter import filedialog

from PyQt5.QtCore import QRegularExpression, Qt
from PyQt5.QtGui import QRegularExpressionValidator, QPixmap
from PyQt5.QtWidgets import QWidget

from client.storage.temporary_storage import TemporaryStorage


class CommonController(TemporaryStorage):
    def only_int(self, qwidget: QWidget):
        """
        숫자만 입력
        :param qwidget: 입력 가능 위젯
        :return:
        """
        regex = QRegularExpression("[0-9_]+")
        validator = QRegularExpressionValidator(regex, self)
        qwidget.setValidator(validator)

    def only_smallalpha_int(self, qwidget: QWidget):
        """
        알파벳, 숫자만 입력
        :param qwidget: 입력 가능 위젯
        :return:
        """
        regex = QRegularExpression("[a-z_,0-9_]+")
        validator = QRegularExpressionValidator(regex, self)
        qwidget.setValidator(validator)

    def only_alpha_int(self, qwidget: QWidget):
        """
        알파벳, 숫자만 입력
        :param qwidget: 입력 가능 위젯
        :return:
        """
        regex = QRegularExpression("[A-Z_,a-z_,0-9_]+")
        validator = QRegularExpressionValidator(regex, self)
        qwidget.setValidator(validator)

    def only_alpha_hangul_int(self, qwidget: QWidget):
        """
        알파벳, 숫자만 입력
        :param qwidget: 입력 가능 위젯
        :return:
        """
        regex = QRegularExpression("[/^[가-힣a-zA-Z0-9]+$/;]+")
        validator = QRegularExpressionValidator(regex, self)
        qwidget.setValidator(validator)

    def btn_set_enable(self, is_ok: bool, qwidget: QWidget):
        """
        버튼 오브젝트 활성화 또는 비활성화
        :param is_ok:
        :param qwidget:
        :return:
        """
        if is_ok:
            qwidget.setDisabled(False)
        else:
            qwidget.setDisabled(True)

    def send_packet(self, p: str):
        """
        서버에 패킷 신호 보내기
        :param p:
        :return:
        """
        if self.info['connect'][0]:
            self.info['socket'][0].send(p.encode())

    def send_json_packet(self, msg: str):
        """
        서버에 제이슨 데이터 보내기
        :param msg: 제이슨 구조
        :return:
        """
        if self.info['connect'][0]:
            self.info['socket'][0].send(bytes(msg, 'UTF-8'))
