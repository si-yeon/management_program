import shutil
import sys
from tkinter import filedialog

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog

from client.controller.controller_common import CommonController
from client.storage.temporary_storage import TemporaryStorage
from client.view.view_register import Ui_Dialog as RegisterView


class RegisterController(QDialog, RegisterView, CommonController, TemporaryStorage):
    def __init__(self, row_data={}):
        super().__init__()
        self.init_setting()
        self.init_variable(row_data)
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

    def init_variable(self, row_data):
        """
        생성자 변수 선언 및 초기화
        """
        self.img_path = '../img/product/question.png'
        self.row_data = row_data
        self.is_save = False

    def init_widget(self):
        """
        생성자 위젯 설정
        """
        if len(self.row_data) != 0:
            path = self.row_data['img'].split('.')
            ext = path[1:]
            if ext == 'png':
                print('1')
                pixmap = QPixmap(path)
            else:
                self.row_data['img'] = self.img_path
                pixmap = QPixmap(self.img_path)
            self.img.setPixmap(pixmap)
            self.img.setScaledContents(True)
            self.img.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.code.setText(self.row_data['code'])
            self.type.setText(self.row_data['type'])
            self.brand.setText(self.row_data['brand'])
            self.name.setText(self.row_data['name'])
            self.purchase_unit_price.setText(self.row_data['purchase_unit_price'])
            self.sales_unit_price.setText(self.row_data['sales_unit_price'])
            self.inventory.setText(self.row_data['inventory'])
            self.safety_inventory.setText(self.row_data['safety_inventory'])

    def init_signal(self):
        """
        생성자 시그널
        """
        self.code.textEdited.connect(lambda txt, key='code': self.input_data(txt, key))
        self.type.textEdited.connect(lambda txt, key='type': self.input_data(txt, key))
        self.brand.textEdited.connect(lambda txt, key='brand': self.input_data(txt, key))
        self.name.textEdited.connect(lambda txt, key='name': self.input_data(txt, key))
        self.purchase_unit_price.textEdited.connect(lambda txt, key='purchase_unit_price': self.input_data(txt, key))
        self.sales_unit_price.textEdited.connect(lambda txt, key='sales_unit_price': self.input_data(txt, key))
        self.inventory.textEdited.connect(lambda txt, key='inventory': self.input_data(txt, key))
        self.safety_inventory.textEdited.connect(lambda txt, key='safety_inventory': self.input_data(txt, key))
        self.pb_load.clicked.connect(self.open_file)
        self.pb_save.clicked.connect(self.save_info)
        self.pb_reset.clicked.connect(self.reset_all)
        self.pb_close.clicked.connect(self.close)

    def init_method(self):
        """
        생성자 함수
        """

    def input_data(self, txt: str, key: str):
        self.row_data[key] = txt

    def save_info(self):
        self.is_save = True
        self.close()

    def open_file(self):
        """
        파일 불러오기 창
        :return:
        """
        try:
            img_path = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
                ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
            file_name = img_path.split('/')[-1]
            file_path = f'../img/product/{file_name}'
            print(file_path)
            self.move_image_file(img_path, file_path)
            self.img_path = file_path
            pixmap = QPixmap(self.img_path)
            self.img.setPixmap(pixmap)
            self.img.setScaledContents(True)
            self.img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        except:
            self.img_path = '../img/product/question.png'

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
        # self.code.clear()
        self.img.clear()
        self.type.clear()
        self.brand.clear()
        self.name.clear()
        self.purchase_unit_price.clear()
        self.sales_unit_price.clear()
        self.inventory.clear()
        self.safety_inventory.clear()

    def closeEvent(self, e):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = RegisterController()
    a.show()
    sys.exit(app.exec_())
