# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_register.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(517, 320)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_product_img = QtWidgets.QLabel(self.widget)
        self.lb_product_img.setMinimumSize(QtCore.QSize(140, 160))
        self.lb_product_img.setMaximumSize(QtCore.QSize(140, 160))
        self.lb_product_img.setObjectName("lb_product_img")
        self.verticalLayout.addWidget(self.lb_product_img)
        self.pb_load = QtWidgets.QPushButton(self.widget)
        self.pb_load.setObjectName("pb_load")
        self.verticalLayout.addWidget(self.pb_load)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.widget_3)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.le_inven = QtWidgets.QLineEdit(self.widget_2)
        self.le_inven.setObjectName("le_inven")
        self.gridLayout.addWidget(self.le_inven, 6, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.le_sales = QtWidgets.QLineEdit(self.widget_2)
        self.le_sales.setObjectName("le_sales")
        self.gridLayout.addWidget(self.le_sales, 5, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 2, 1)
        self.le_purchase = QtWidgets.QLineEdit(self.widget_2)
        self.le_purchase.setObjectName("le_purchase")
        self.gridLayout.addWidget(self.le_purchase, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.le_safety_inven = QtWidgets.QLineEdit(self.widget_2)
        self.le_safety_inven.setObjectName("le_safety_inven")
        self.gridLayout.addWidget(self.le_safety_inven, 7, 1, 2, 1)
        self.le_name = QtWidgets.QLineEdit(self.widget_2)
        self.le_name.setObjectName("le_name")
        self.gridLayout.addWidget(self.le_name, 3, 1, 1, 1)
        self.le_brand = QtWidgets.QLineEdit(self.widget_2)
        self.le_brand.setObjectName("le_brand")
        self.gridLayout.addWidget(self.le_brand, 2, 1, 1, 1)
        self.cb_type = QtWidgets.QComboBox(self.widget_2)
        self.cb_type.setObjectName("cb_type")
        self.gridLayout.addWidget(self.cb_type, 1, 1, 1, 1)
        self.le_code = QtWidgets.QLineEdit(self.widget_2)
        self.le_code.setObjectName("le_code")
        self.gridLayout.addWidget(self.le_code, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(Dialog)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb_save = QtWidgets.QPushButton(self.widget_4)
        self.pb_save.setObjectName("pb_save")
        self.horizontalLayout_2.addWidget(self.pb_save, 0, QtCore.Qt.AlignHCenter)
        self.pb_reset = QtWidgets.QPushButton(self.widget_4)
        self.pb_reset.setObjectName("pb_reset")
        self.horizontalLayout_2.addWidget(self.pb_reset, 0, QtCore.Qt.AlignHCenter)
        self.pb_close = QtWidgets.QPushButton(self.widget_4)
        self.pb_close.setObjectName("pb_close")
        self.horizontalLayout_2.addWidget(self.pb_close, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.widget_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lb_product_img.setText(_translate("Dialog", "이미지"))
        self.pb_load.setText(_translate("Dialog", "불러오기"))
        self.label_4.setText(_translate("Dialog", "분류"))
        self.label_6.setText(_translate("Dialog", "구매단가"))
        self.label_8.setText(_translate("Dialog", "재고"))
        self.label_3.setText(_translate("Dialog", "브랜드"))
        self.label_9.setText(_translate("Dialog", "안전재고"))
        self.label_2.setText(_translate("Dialog", "상품코드"))
        self.label_7.setText(_translate("Dialog", "판매단가"))
        self.label_5.setText(_translate("Dialog", "상품명"))
        self.pb_save.setText(_translate("Dialog", "저장"))
        self.pb_reset.setText(_translate("Dialog", "다시작성"))
        self.pb_close.setText(_translate("Dialog", "닫기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
