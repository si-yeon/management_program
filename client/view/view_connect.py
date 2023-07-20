# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_connect.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(285, 180)
        Dialog.setMinimumSize(QtCore.QSize(0, 180))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 180))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setStyleSheet("QWidget{\n"
"font-family: Pretendard;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid #164DCA;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"border-bottom:none;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Pretendard")
        font.setBold(True)
        font.setWeight(62)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: none;\n"
"border-radius: 0;\n"
"font-weight:500;\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.le_ip = QtWidgets.QLineEdit(self.widget_2)
        self.le_ip.setStyleSheet("QLineEdit{\n"
"border: none; \n"
"border-bottom: 2px solid #164DCA;\n"
"background-color: transparent;\n"
"font-size: 20px;\n"
"text-align: center;\n"
"font-weight:500;\n"
"}\n"
"\n"
"\n"
"")
        self.le_ip.setObjectName("le_ip")
        self.horizontalLayout_3.addWidget(self.le_ip)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setStyleSheet("QWidget{\n"
"font-family: Pretendard;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid #164DCA;\n"
"border-top:none;\n"
"border-bottom:none;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Pretendard")
        font.setBold(True)
        font.setWeight(62)
        self.label.setFont(font)
        self.label.setStyleSheet("border: none;\n"
"border-radius: 0;\n"
"font-weight:500;\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.le_port = QtWidgets.QLineEdit(self.widget_3)
        self.le_port.setStyleSheet("QLineEdit{\n"
"border: none; \n"
"border-bottom: 2px solid #164DCA;\n"
"background-color: transparent;\n"
"font-size: 20px;\n"
"text-align: center;\n"
"font-weight:500;\n"
"}\n"
"\n"
"\n"
"")
        self.le_port.setObjectName("le_port")
        self.horizontalLayout.addWidget(self.le_port)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(Dialog)
        self.widget_4.setStyleSheet("QWidget{\n"
"font-family: Pretendard;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid #164DCA;\n"
"border-bottom-left-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"border-top:none;\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb_connect = QtWidgets.QPushButton(self.widget_4)
        self.pb_connect.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Pretendard")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pb_connect.setFont(font)
        self.pb_connect.setStyleSheet("QPushButton{\n"
"background: #164DCA;\n"
"box-shadow: 0px 2px 12px rgb(25 25 25 / 16%);\n"
"align-items: center;\n"
"color: #fff;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"border-radius: 10px;\n"
"padding: 6px;\n"
"}")
        self.pb_connect.setObjectName("pb_connect")
        self.horizontalLayout_2.addWidget(self.pb_connect, 0, QtCore.Qt.AlignHCenter)
        self.pb_close = QtWidgets.QPushButton(self.widget_4)
        self.pb_close.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Pretendard")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pb_close.setFont(font)
        self.pb_close.setStyleSheet("QPushButton{\n"
"background: #164DCA;\n"
"box-shadow: 0px 2px 12px rgb(25 25 25 / 16%);\n"
"align-items: center;\n"
"color: #fff;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"border-radius: 10px;\n"
"padding: 6px;\n"
"}")
        self.pb_close.setObjectName("pb_close")
        self.horizontalLayout_2.addWidget(self.pb_close, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget_4)

        self.retranslateUi(Dialog)
        self.pb_close.clicked.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "IP : "))
        self.le_ip.setText(_translate("Dialog", "localhost"))
        self.label.setText(_translate("Dialog", "PORT : "))
        self.le_port.setText(_translate("Dialog", "5000"))
        self.pb_connect.setText(_translate("Dialog", "연결"))
        self.pb_close.setText(_translate("Dialog", "종료"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
