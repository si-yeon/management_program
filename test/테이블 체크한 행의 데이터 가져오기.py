from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, \
    QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checked Rows Data")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Checkbox", "Column 1", "Column 2"])

        for i in range(5):
            checkbox_item = QTableWidgetItem()
            checkbox_item.setFlags(checkbox_item.flags() | Qt.ItemIsUserCheckable)
            checkbox_item.setCheckState(Qt.Unchecked)

            item1 = QTableWidgetItem(f"Row {i + 1}, Col 1")
            item2 = QTableWidgetItem(f"Row {i + 1}, Col 2")

            self.tableWidget.setItem(i, 0, checkbox_item)
            self.tableWidget.setItem(i, 1, item1)
            self.tableWidget.setItem(i, 2, item2)

        layout.addWidget(self.tableWidget)

        button = QPushButton("Get Checked Rows Data", self)
        button.clicked.connect(self.get_checked_rows_data)
        layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def get_checked_rows_data(self):
        checked_data = []
        for row in range(self.tableWidget.rowCount()):
            checkbox_item = self.tableWidget.item(row, 0)
            if checkbox_item.checkState() == Qt.Checked:
                data1 = self.tableWidget.item(row, 1).text()
                data2 = self.tableWidget.item(row, 2).text()
                checked_data.append((data1, data2))

        print("Checked Rows Data:")
        for data in checked_data:
            print(data)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
