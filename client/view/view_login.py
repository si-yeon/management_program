# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(322, 397)
        Form.setStyleSheet("font-family: Pretendard;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lb_logo = QtWidgets.QLabel(self.frame)
        self.lb_logo.setObjectName("lb_logo")
        self.verticalLayout_3.addWidget(self.lb_logo, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.le_id = QtWidgets.QLineEdit(self.frame_2)
        self.le_id.setStyleSheet("QLineEdit{\n"
"border: none; \n"
"border-bottom: 2px solid #212529;\n"
"background-color: transparent;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"")
        self.le_id.setText("")
        self.le_id.setObjectName("le_id")
        self.verticalLayout_4.addWidget(self.le_id)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.le_pw = QtWidgets.QLineEdit(self.frame_3)
        self.le_pw.setStyleSheet("QLineEdit{\n"
"border: none; \n"
"border-bottom: 2px solid #212529;\n"
"background-color: transparent;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"")
        self.le_pw.setText("")
        self.le_pw.setObjectName("le_pw")
        self.verticalLayout_5.addWidget(self.le_pw)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_6 = QtWidgets.QFrame(Form)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lb_warning = QtWidgets.QLabel(self.frame_6)
        self.lb_warning.setText("")
        self.lb_warning.setObjectName("lb_warning")
        self.verticalLayout_6.addWidget(self.lb_warning, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb_auto_fill = QtWidgets.QCheckBox(self.frame_5)
        self.cb_auto_fill.setStyleSheet("font-size: 15px;")
        self.cb_auto_fill.setObjectName("cb_auto_fill")
        self.horizontalLayout.addWidget(self.cb_auto_fill, 0, QtCore.Qt.AlignHCenter)
        self.cb_remember_id = QtWidgets.QCheckBox(self.frame_5)
        self.cb_remember_id.setStyleSheet("font-size: 15px;")
        self.cb_remember_id.setObjectName("cb_remember_id")
        self.horizontalLayout.addWidget(self.cb_remember_id, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb_login = QtWidgets.QPushButton(self.frame_4)
        self.pb_login.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Pretendard")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pb_login.setFont(font)
        self.pb_login.setStyleSheet("border: 2px solid #212529;\n"
"    background-color: #fff;\n"
"    color: #212529;\n"
"    font-weight: 500;\n"
"    font-size: 20px;\n"
"    border-top-left-radius: 0.3rem;\n"
"    border-top-right-radius: 0.3rem;\n"
"\n"
"")
        self.pb_login.setObjectName("pb_login")
        self.horizontalLayout_2.addWidget(self.pb_login, 0, QtCore.Qt.AlignHCenter)
        self.pb_member = QtWidgets.QPushButton(self.frame_4)
        self.pb_member.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Pretendard")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pb_member.setFont(font)
        self.pb_member.setStyleSheet("border: 2px solid #212529;\n"
"    background-color: #fff;\n"
"    color: #212529;\n"
"    font-weight: 500;\n"
"    font-size: 20px;\n"
"    border-top-left-radius: 0.3rem;\n"
"    border-top-right-radius: 0.3rem;\n"
"\n"
"")
        self.pb_member.setObjectName("pb_member")
        self.horizontalLayout_2.addWidget(self.pb_member, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "login"))
        self.lb_logo.setText(_translate("Form", "LOGO"))
        self.cb_auto_fill.setText(_translate("Form", "자동완성"))
        self.cb_remember_id.setText(_translate("Form", "아이디 저장"))
        self.pb_login.setText(_translate("Form", "로그인"))
        self.pb_member.setText(_translate("Form", "회원가입"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
