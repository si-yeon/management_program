# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"background-color: #fff;\n"
"}\n"
"QPushButton{\n"
"background: #164DCA;\n"
"box-shadow: 0px 2px 12px rgb(25 25 25 / 16%);\n"
"align-items: center;\n"
"color: #fff;\n"
"font-weight: 600;\n"
"font-size: 20px;\n"
"border-radius: 10px;\n"
"padding: 6px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 6)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lb_no_read = QtWidgets.QLabel(self.widget_4)
        self.lb_no_read.setObjectName("lb_no_read")
        self.horizontalLayout_11.addWidget(self.lb_no_read)
        self.pb_chat = QtWidgets.QPushButton(self.widget_4)
        self.pb_chat.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_chat.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.pb_chat.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../img/icon/chat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_chat.setIcon(icon)
        self.pb_chat.setIconSize(QtCore.QSize(30, 30))
        self.pb_chat.setObjectName("pb_chat")
        self.horizontalLayout_11.addWidget(self.pb_chat)
        self.horizontalLayout.addLayout(self.horizontalLayout_11)
        self.pb_timeline = QtWidgets.QPushButton(self.widget_4)
        self.pb_timeline.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_timeline.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.pb_timeline.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../img/icon/time.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_timeline.setIcon(icon1)
        self.pb_timeline.setIconSize(QtCore.QSize(30, 30))
        self.pb_timeline.setObjectName("pb_timeline")
        self.horizontalLayout.addWidget(self.pb_timeline)
        self.pb_profile = QtWidgets.QPushButton(self.widget_4)
        self.pb_profile.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_profile.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.pb_profile.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../img/icon/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_profile.setIcon(icon2)
        self.pb_profile.setIconSize(QtCore.QSize(30, 30))
        self.pb_profile.setObjectName("pb_profile")
        self.horizontalLayout.addWidget(self.pb_profile)
        self.pb_logout = QtWidgets.QPushButton(self.widget_4)
        self.pb_logout.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_logout.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.pb_logout.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../img/icon/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_logout.setIcon(icon3)
        self.pb_logout.setIconSize(QtCore.QSize(30, 30))
        self.pb_logout.setObjectName("pb_logout")
        self.horizontalLayout.addWidget(self.pb_logout)
        self.horizontalLayout_2.addWidget(self.widget_4, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_9 = QtWidgets.QWidget(self.centralwidget)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 9)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_8 = QtWidgets.QWidget(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout.setContentsMargins(0, 9, 0, 9)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_10 = QtWidgets.QWidget(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.widget_10)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setContentsMargins(9, 9, 0, 9)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pb_excel = QtWidgets.QPushButton(self.widget)
        self.pb_excel.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_excel.setStyleSheet("")
        self.pb_excel.setText("")
        self.pb_excel.setIconSize(QtCore.QSize(20, 20))
        self.pb_excel.setObjectName("pb_excel")
        self.horizontalLayout_7.addWidget(self.pb_excel, 0, QtCore.Qt.AlignLeft)
        self.pb_shortage_check = QtWidgets.QPushButton(self.widget)
        self.pb_shortage_check.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_shortage_check.setObjectName("pb_shortage_check")
        self.horizontalLayout_7.addWidget(self.pb_shortage_check)
        self.pb_inven_check = QtWidgets.QPushButton(self.widget)
        self.pb_inven_check.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_inven_check.setObjectName("pb_inven_check")
        self.horizontalLayout_7.addWidget(self.pb_inven_check)
        self.widget_11 = QtWidgets.QWidget(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.widget_11.setFont(font)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_7.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.widget)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.le_find = QtWidgets.QLineEdit(self.widget_12)
        self.le_find.setMinimumSize(QtCore.QSize(200, 30))
        self.le_find.setStyleSheet("    text-align: center;\n"
"    border: 1px solid #164DCA;\n"
"    border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"font-size: 15px;\n"
"")
        self.le_find.setObjectName("le_find")
        self.horizontalLayout_6.addWidget(self.le_find, 0, QtCore.Qt.AlignRight)
        self.pb_find = QtWidgets.QPushButton(self.widget_12)
        self.pb_find.setMinimumSize(QtCore.QSize(75, 30))
        self.pb_find.setStyleSheet("border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;")
        self.pb_find.setText("")
        self.pb_find.setIconSize(QtCore.QSize(20, 20))
        self.pb_find.setObjectName("pb_find")
        self.horizontalLayout_6.addWidget(self.pb_find, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_7.addWidget(self.widget_12)
        self.verticalLayout_3.addWidget(self.widget, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.tableWidget = QtWidgets.QTableWidget(self.widget_10)
        self.tableWidget.setStyleSheet("    text-align: center;\n"
"    border: 1px solid #164DCA;\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.widget_10)
        self.widget_3 = QtWidgets.QWidget(self.widget_8)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pb_add = QtWidgets.QPushButton(self.widget_3)
        self.pb_add.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_add.setObjectName("pb_add")
        self.horizontalLayout_4.addWidget(self.pb_add)
        self.pb_update = QtWidgets.QPushButton(self.widget_3)
        self.pb_update.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_update.setObjectName("pb_update")
        self.horizontalLayout_4.addWidget(self.pb_update)
        self.pb_delete = QtWidgets.QPushButton(self.widget_3)
        self.pb_delete.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_delete.setObjectName("pb_delete")
        self.horizontalLayout_4.addWidget(self.pb_delete)
        self.pb_take_In = QtWidgets.QPushButton(self.widget_3)
        self.pb_take_In.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_take_In.setObjectName("pb_take_In")
        self.horizontalLayout_4.addWidget(self.pb_take_In)
        self.pb_take_out = QtWidgets.QPushButton(self.widget_3)
        self.pb_take_out.setMinimumSize(QtCore.QSize(0, 0))
        self.pb_take_out.setObjectName("pb_take_out")
        self.horizontalLayout_4.addWidget(self.pb_take_out)
        self.verticalLayout.addWidget(self.widget_3, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_3.addWidget(self.widget_8)
        self.widget_7 = QtWidgets.QWidget(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_7.setMaximumSize(QtCore.QSize(400, 16777215))
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stack_view = QtWidgets.QStackedWidget(self.widget_7)
        self.stack_view.setObjectName("stack_view")
        self.page_chat = QtWidgets.QWidget()
        self.page_chat.setObjectName("page_chat")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_chat)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lw_chat_room = QtWidgets.QListWidget(self.page_chat)
        self.lw_chat_room.setStyleSheet("QScrollBar\n"
"{\n"
"background : white;\n"
"}\n"
"QScrollBar::handle\n"
"{\n"
"background : #164DCA;\n"
"}\n"
"QScrollBar::handle::pressed\n"
"{\n"
"background : #164DCA;\n"
"}\n"
"QScrollArea\n"
"{\n"
"background-color: white;\n"
"border: none;\n"
"}\n"
"\n"
"QListWidget{\n"
"    text-align: center;\n"
"    border: 1px solid #164DCA;\n"
"}")
        self.lw_chat_room.setObjectName("lw_chat_room")
        self.verticalLayout_5.addWidget(self.lw_chat_room)
        self.widget_13 = QtWidgets.QWidget(self.page_chat)
        self.widget_13.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.le_msg = QtWidgets.QLineEdit(self.widget_13)
        self.le_msg.setMinimumSize(QtCore.QSize(0, 40))
        self.le_msg.setStyleSheet("    text-align: center;\n"
"    border: 1px solid #164DCA;\n"
"    border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"font-size: 15px;\n"
"")
        self.le_msg.setObjectName("le_msg")
        self.horizontalLayout_8.addWidget(self.le_msg)
        self.pb_send = QtWidgets.QPushButton(self.widget_13)
        self.pb_send.setMinimumSize(QtCore.QSize(0, 40))
        self.pb_send.setStyleSheet("border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;")
        self.pb_send.setObjectName("pb_send")
        self.horizontalLayout_8.addWidget(self.pb_send)
        self.verticalLayout_5.addWidget(self.widget_13)
        self.stack_view.addWidget(self.page_chat)
        self.page_profile = QtWidgets.QWidget()
        self.page_profile.setStyleSheet("  text-align: center;\n"
"    border: 1px solid #164DCA;\n"
"    border-radius: 15px;")
        self.page_profile.setObjectName("page_profile")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_profile)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_14 = QtWidgets.QWidget(self.page_profile)
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_14)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_17 = QtWidgets.QWidget(self.widget_14)
        self.widget_17.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.widget_17)
        self.label_2.setMinimumSize(QtCore.QSize(90, 120))
        self.label_2.setMaximumSize(QtCore.QSize(90, 120))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget_17)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.verticalLayout_8.addWidget(self.widget_17)
        self.textEdit = QtWidgets.QTextEdit(self.widget_14)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_8.addWidget(self.textEdit)
        self.verticalLayout_7.addWidget(self.widget_14, 0, QtCore.Qt.AlignTop)
        self.widget_15 = QtWidgets.QWidget(self.page_profile)
        self.widget_15.setObjectName("widget_15")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_15)
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.widget_15)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget_15)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_15)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_15)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget_15)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_15)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_15)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget_15)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 1, 1, 1)
        self.verticalLayout_7.addWidget(self.widget_15)
        self.widget_16 = QtWidgets.QWidget(self.page_profile)
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_7.addWidget(self.widget_16)
        self.stack_view.addWidget(self.page_profile)
        self.page_timeline = QtWidgets.QWidget()
        self.page_timeline.setObjectName("page_timeline")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_timeline)
        self.verticalLayout_6.setContentsMargins(9, 0, 9, 9)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lw_time_line = QtWidgets.QListWidget(self.page_timeline)
        self.lw_time_line.setStyleSheet("    text-align: center;\n"
"    border: 1px solid #164DCA;\n"
"    border-radius: 15px;")
        self.lw_time_line.setObjectName("lw_time_line")
        self.verticalLayout_6.addWidget(self.lw_time_line)
        self.stack_view.addWidget(self.page_timeline)
        self.verticalLayout_4.addWidget(self.stack_view)
        self.horizontalLayout_3.addWidget(self.widget_7)
        self.verticalLayout_2.addWidget(self.widget_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.menu.addAction(self.actionclose)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.stack_view.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_no_read.setText(_translate("MainWindow", "안 읽음"))
        self.pb_chat.setToolTip(_translate("MainWindow", "채팅"))
        self.pb_timeline.setToolTip(_translate("MainWindow", "타임라인"))
        self.pb_profile.setToolTip(_translate("MainWindow", "내 정보"))
        self.pb_logout.setToolTip(_translate("MainWindow", "로그아웃"))
        self.pb_shortage_check.setText(_translate("MainWindow", "재고부족"))
        self.pb_inven_check.setText(_translate("MainWindow", "재고현황"))
        self.pb_add.setText(_translate("MainWindow", "추가"))
        self.pb_update.setText(_translate("MainWindow", "수정"))
        self.pb_delete.setText(_translate("MainWindow", "삭제"))
        self.pb_take_In.setText(_translate("MainWindow", "입고"))
        self.pb_take_out.setText(_translate("MainWindow", "출고"))
        self.pb_send.setText(_translate("MainWindow", "전송"))
        self.label_2.setText(_translate("MainWindow", "사진"))
        self.label_3.setText(_translate("MainWindow", "아이디"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "입사일"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "부서"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "직급"))
        self.label_4.setText(_translate("MainWindow", "성명"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.menu.setTitle(_translate("MainWindow", "메뉴"))
        self.actionclose.setText(_translate("MainWindow", "close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
