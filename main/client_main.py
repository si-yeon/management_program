import sys

from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QApplication, QMessageBox

from client.controller.controller_connect import ConnectController
from client.controller.controller_login import LoginController
from client.controller.controller_mainwindow import MainWindowController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fontDB = QFontDatabase()
    fontDB.addApplicationFont('../font/Pretendard-Regular.ttf')
    app.setFont(QFont('Pretendard'))
    conn_server = ConnectController()
    conn_server.exec()
    if conn_server.connected:
        login_view = LoginController()
        login_view.exec()
        if login_view.is_ok:
            main = MainWindowController()
            main.show()
    else:
        sys.exit()
    sys.excepthook = lambda exctype, value, traceback: show_error_message(str(value), traceback)
    sys.exit(app.exec())

def show_error_message(message, traceback):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle("Error")
    msg_box.setText(message)
    msg_box.exec_()
    traceback.print_exc()

