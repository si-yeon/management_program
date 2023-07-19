import shutil
import sys
from tkinter import filedialog

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog

from client.storage.temporary_storage import TemporaryStorage
from client.view.view_register import Ui_Dialog as RegisterView


class RegisterController(QDialog, RegisterView, TemporaryStorage):
    def __init__(self, dict_data = {}):
        super().__init__()
        self.init_setting()
        self.init_variable(dict_data)
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

    def init_variable(self,dict_data):
        """
        생성자 변수 선언 및 초기화
        """
        self.img_path = '../../img/product/question.png'






    def init_widget(self):
        """
        생성자 위젯 설정
        """
        pixmap = QPixmap(self.img_path)
        self.lb_product_img.setPixmap(pixmap)
        self.lb_product_img.setScaledContents(True)
        self.lb_product_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def init_signal(self):
        """
        생성자 시그널
        """
        self.pb_load.clicked.connect(self.open_file)
        self.pb_save.clicked.connect(self.close)
        self.pb_reset.clicked.connect(self.reset_all)
        self.pb_close.clicked.connect(self.close)

    def init_method(self):
        """
        생성자 함수
        """

    def open_file(self):
        """
        파일 불러오기 창
        :return:
        """
        try:
            img_path = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
                ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
            file_name = img_path.split('/')[-1]
            file_path = f'../../img/product/{file_name}'
            self.move_image_file(img_path, file_path)
            self.img_path = file_path
            pixmap = QPixmap(self.img_path)
            self.lb_product_img.setPixmap(pixmap)
            self.lb_product_img.setScaledContents(True)
            self.lb_product_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        except:
            self.img_path = '../../img/product/question.png'

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
            pass

    def reset_all(self):
        self.lb_product_img.clear()
        self.le_code.clear()
        self.cb_type.clear()
        self.le_brand.clear()
        self.le_name.clear()
        self.le_purchase.clear()
        self.le_sales.clear()
        self.le_inven.clear()
        self.le_safety_inven.clear()

    def send_packet(self, p):
        if self.info['connect'][0]:
            self.info['socket'][0].send(p.encode("UTF-8"))

    def closeEvent(self, e):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = RegisterController()
    a.show()
    sys.exit(app.exec_())
