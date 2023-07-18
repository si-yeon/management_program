from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator
from PyQt5.QtWidgets import QWidget


class CommonController:
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
        if is_ok:
            qwidget.setDisabled(False)
        else:
            qwidget.setDisabled(True)
