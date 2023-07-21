import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPixmap

class CircleButton(QPushButton):
    # 테두리기 동그란 버튼
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.resize(10,10)

        # Customize the button's appearance
        self.setStyleSheet("""
            QPushButton {
                 border-radius: 25%;
                 color: #fff;
                 font-size: 10px;
                 font-weight: 1000;
                 border: 1px solid red;
                text-align: center;
                background: red;
            }
        """)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow('1')
    window.show()
    sys.exit(app.exec_())
