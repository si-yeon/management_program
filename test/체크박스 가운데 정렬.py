from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, \
    QWidget, QStyledItemDelegate, QStyle, QStyleOptionButton


class CheckBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        return None

    def paint(self, painter, option, index):
        if index.column() == 0:
            style_option = QStyleOptionButton()
            style_option.state |= QStyle.State_Enabled

            if index.data(Qt.CheckStateRole) == Qt.Checked:
                style_option.state |= QStyle.State_On
            else:
                style_option.state |= QStyle.State_Off

            style_option.rect = option.rect
            style_option.rect.center()

            self.parent().style().drawControl(QStyle.CE_CheckBox, style_option, painter)
        else:
            super().paint(painter, option, index)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget with Centered Checkboxes")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Checkbox Column", "Data"])

        # Set the custom delegate to the first column
        self.tableWidget.setItemDelegateForColumn(0, CheckBoxDelegate(self))

        layout.addWidget(self.tableWidget)

        button = QPushButton("Add New Row", self)
        button.clicked.connect(self.add_new_row)
        layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_new_row(self):
        row_count = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row_count + 1)

        # Create a checkbox item
        checkbox_item = QTableWidgetItem()
        checkbox_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        checkbox_item.setCheckState(Qt.Unchecked)

        self.tableWidget.setItem(row_count, 0, checkbox_item)
        self.tableWidget.setItem(row_count, 1, QTableWidgetItem("New Row, Data"))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
