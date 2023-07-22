# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_membership.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(555, 312)
        Dialog.setStyleSheet("font-family: Pretendard;\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setStyleSheet("QWidget{\n"
"border: 2px solid #164DCA;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"border-bottom:none;\n"
"}\n"
"QFrame{\n"
"border: none;\n"
"border-radius: 0px;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setContentsMargins(9, 9, 9, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame = QtWidgets.QFrame(self.widget_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(30, 0, 0, 10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalFrame = QtWidgets.QFrame(self.frame)
        self.verticalFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lb_profile_img = QtWidgets.QLabel(self.verticalFrame)
        self.lb_profile_img.setMinimumSize(QtCore.QSize(150, 180))
        self.lb_profile_img.setStyleSheet("border: 2px dashed  #164DCA;")
        self.lb_profile_img.setText("")
        self.lb_profile_img.setObjectName("lb_profile_img")
        self.verticalLayout_7.addWidget(self.lb_profile_img, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addWidget(self.verticalFrame, 0, QtCore.Qt.AlignHCenter)
        self.pb_regist_img = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_regist_img.sizePolicy().hasHeightForWidth())
        self.pb_regist_img.setSizePolicy(sizePolicy)
        self.pb_regist_img.setMinimumSize(QtCore.QSize(100, 30))
        self.pb_regist_img.setMaximumSize(QtCore.QSize(16777215, 35))
        self.pb_regist_img.setStyleSheet("QPushButton{\n"
"background: #164DCA;\n"
"box-shadow: 0px 2px 12px rgb(25 25 25 / 16%);\n"
"align-items: center;\n"
"color: #fff;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"border-radius: 10px;\n"
"padding: 6px;\n"
"}")
        self.pb_regist_img.setObjectName("pb_regist_img")
        self.verticalLayout_4.addWidget(self.pb_regist_img, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_8.addWidget(self.frame)
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setContentsMargins(30, 0, 30, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.le_id = QtWidgets.QLineEdit(self.frame_2)
        self.le_id.setMinimumSize(QtCore.QSize(0, 35))
        self.le_id.setStyleSheet("QLineEdit{\n"
"border: none; \n"
"border-top: 2px solid  #164DCA;\n"
"border-left: 2px solid  #164DCA;\n"
"border-right: 2px solid  #164DCA;\n"
"background-color: transparent;\n"
"font-size: 20px;\n"
"}\n"
"")
        self.le_id.setText("")
        self.le_id.setObjectName("le_id")
        self.verticalLayout_5.addWidget(self.le_id)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setContentsMargins(30, 0, 30, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.le_pw = QtWidgets.QLineEdit(self.frame_3)
        self.le_pw.setMinimumSize(QtCore.QSize(0, 35))
        self.le_pw.setStyleSheet("QLineEdit{\n"
"border: none; \n"
"border-top: 2px solid  #164DCA;\n"
"border-left: 2px solid  #164DCA;\n"
"border-right: 2px solid  #164DCA;\n"
"background-color: transparent;\n"
"font-size: 20px;\n"
"}\n"
"")
        self.le_pw.setText("")
        self.le_pw.setObjectName("le_pw")
        self.verticalLayout_6.addWidget(self.le_pw)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.widget)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.le_name = QtWidgets.QLineEdit(self.frame_5)
        self.le_name.setMinimumSize(QtCore.QSize(0, 35))
        self.le_name.setStyleSheet("QLineEdit{\n"
"border: none; \n"
"border-top: 2px solid  #164DCA;\n"
"border-left: 2px solid  #164DCA;\n"
"border-right: 2px solid  #164DCA;\n"
"background-color: transparent;\n"
"font-size: 20px;\n"
"}\n"
"")
        self.le_name.setText("")
        self.le_name.setObjectName("le_name")
        self.horizontalLayout.addWidget(self.le_name)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(self.widget)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.le_depart = QtWidgets.QLineEdit(self.frame_7)
        self.le_depart.setMinimumSize(QtCore.QSize(0, 35))
        self.le_depart.setStyleSheet("QLineEdit{\n"
"border: none; \n"
"border-top: 2px solid  #164DCA;\n"
"border-left: 2px solid  #164DCA;\n"
"border-right: 2px solid  #164DCA;\n"
"background-color: transparent;\n"
"font-size: 20px;\n"
"}\n"
"")
        self.le_depart.setText("")
        self.le_depart.setObjectName("le_depart")
        self.horizontalLayout_6.addWidget(self.le_depart)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.widget)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setContentsMargins(30, 0, 30, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.le_position = QtWidgets.QLineEdit(self.frame_8)
        self.le_position.setMinimumSize(QtCore.QSize(0, 35))
        self.le_position.setStyleSheet("QLineEdit{\n"
"border: none; \n"
"border-top: 2px solid  #164DCA;\n"
"border-left: 2px solid  #164DCA;\n"
"border-right: 2px solid  #164DCA;\n"
"background-color: transparent;\n"
"font-size: 20px;\n"
"}\n"
"")
        self.le_position.setText("")
        self.le_position.setObjectName("le_position")
        self.horizontalLayout_7.addWidget(self.le_position)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_6 = QtWidgets.QFrame(self.widget)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lw_msg = QtWidgets.QListWidget(self.frame_6)
        self.lw_msg.setMinimumSize(QtCore.QSize(0, 35))
        self.lw_msg.setStyleSheet("border-bottom: 2px solid  #164DCA;\n"
"border-left: 2px solid  #164DCA;\n"
"border-right: 2px solid  #164DCA;\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"background-color: transparent;")
        self.lw_msg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lw_msg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lw_msg.setObjectName("lw_msg")
        self.horizontalLayout_4.addWidget(self.lw_msg)
        self.verticalLayout.addWidget(self.frame_6)
        self.horizontalLayout_8.addWidget(self.widget)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(Dialog)
        self.widget_4.setStyleSheet("QWidget{\n"
"border: 2px solid #164DCA;\n"
"border-bottom-left-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"border-top:none;\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb_join = QtWidgets.QPushButton(self.widget_4)
        self.pb_join.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Pretendard")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pb_join.setFont(font)
        self.pb_join.setStyleSheet("border: 2px solid #164DCA;\n"
"    background-color: #fff;\n"
"    color: #164DCA;\n"
"    font-weight: 500;\n"
"    font-size: 20px;\n"
"    border-radius: 0.5rem;\n"
"\n"
"\n"
"")
        self.pb_join.setObjectName("pb_join")
        self.horizontalLayout_2.addWidget(self.pb_join, 0, QtCore.Qt.AlignHCenter)
        self.pb_member = QtWidgets.QPushButton(self.widget_4)
        self.pb_member.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Pretendard")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pb_member.setFont(font)
        self.pb_member.setStyleSheet("border: 2px solid #164DCA;\n"
"    background-color: #fff;\n"
"    color: #164DCA;\n"
"    font-weight: 500;\n"
"    font-size: 20px;\n"
"    border-radius: 0.5rem;\n"
"\n"
"\n"
"")
        self.pb_member.setObjectName("pb_member")
        self.horizontalLayout_2.addWidget(self.pb_member, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.widget_4)

        self.retranslateUi(Dialog)
        self.pb_member.clicked.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pb_regist_img.setText(_translate("Dialog", "사진등록"))
        self.le_id.setPlaceholderText(_translate("Dialog", "아이디"))
        self.le_pw.setPlaceholderText(_translate("Dialog", "비밀번호"))
        self.le_name.setPlaceholderText(_translate("Dialog", "이름"))
        self.le_depart.setPlaceholderText(_translate("Dialog", "부서"))
        self.le_position.setPlaceholderText(_translate("Dialog", "직책"))
        self.pb_join.setText(_translate("Dialog", "회원가입"))
        self.pb_member.setText(_translate("Dialog", "취소"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
