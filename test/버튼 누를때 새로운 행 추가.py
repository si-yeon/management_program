from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add New Row")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Column 1", "Column 2"])

        layout.addWidget(self.tableWidget)

        button = QPushButton("Add New Row", self)
        button.clicked.connect(self.add_new_row)
        layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_new_row(self):
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.setItem(row_count, i, QTableWidgetItem(f"New Row, Col {i}"))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
