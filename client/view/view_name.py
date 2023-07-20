# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_name.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(311, 180)
        Dialog.setMinimumSize(QtCore.QSize(0, 180))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 180))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 120))
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
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.le_file_name = QtWidgets.QLineEdit(self.widget_2)
        self.le_file_name.setMinimumSize(QtCore.QSize(250, 0))
        self.le_file_name.setStyleSheet("    text-align: center;\n"
"    border: 1px solid #164DCA;\n"
"font-size: 23px;\n"
"border: none;\n"
"border-bottom: 2px solid #164DCA;")
        self.le_file_name.setObjectName("le_file_name")
        self.horizontalLayout_3.addWidget(self.le_file_name, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(Dialog)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 60))
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
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb_check = QtWidgets.QPushButton(self.widget_4)
        self.pb_check.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Pretendard")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pb_check.setFont(font)
        self.pb_check.setStyleSheet("QPushButton{\n"
"background: #164DCA;\n"
"box-shadow: 0px 2px 12px rgb(25 25 25 / 16%);\n"
"align-items: center;\n"
"color: #fff;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"border-radius: 10px;\n"
"padding: 6px;\n"
"}")
        self.pb_check.setObjectName("pb_check")
        self.horizontalLayout_2.addWidget(self.pb_check, 0, QtCore.Qt.AlignHCenter)
        self.pb_cancel = QtWidgets.QPushButton(self.widget_4)
        self.pb_cancel.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Pretendard")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pb_cancel.setFont(font)
        self.pb_cancel.setStyleSheet("QPushButton{\n"
"background: #164DCA;\n"
"box-shadow: 0px 2px 12px rgb(25 25 25 / 16%);\n"
"align-items: center;\n"
"color: #fff;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"border-radius: 10px;\n"
"padding: 6px;\n"
"}")
        self.pb_cancel.setObjectName("pb_cancel")
        self.horizontalLayout_2.addWidget(self.pb_cancel, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget_4)

        self.retranslateUi(Dialog)
        self.pb_check.clicked.connect(Dialog.accept) # type: ignore
        self.pb_cancel.clicked.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.le_file_name.setPlaceholderText(_translate("Dialog", "파일명을 입력해주세요."))
        self.pb_check.setText(_translate("Dialog", "확인"))
        self.pb_cancel.setText(_translate("Dialog", "취소"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
