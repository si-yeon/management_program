from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Data Example")
        self.setGeometry(100, 100, 600, 400)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(['Name', 'Age', 'Country'])

        self.populate_table()

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table_widget)

        # Main widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Get table data
        self.get_table_data()

    def populate_table(self):
        self.table_widget.setRowCount(3)

        # Example data
        data = [
            ['John Doe', '25', 'USA'],
            ['Jane Smith', '30', 'Canada'],
            ['David Johnson', '35', 'USA'],
        ]

        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(value)
                self.table_widget.setItem(row, col, item)

    def get_table_data(self):
        table_data = []
        for row in range(self.table_widget.rowCount()):
            row_data = []
            for col in range(self.table_widget.columnCount()):
                item = self.table_widget.item(row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append('')
            table_data.append(row_data)

        print(table_data)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()

    app.exec_()
