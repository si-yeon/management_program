from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Modification Example")
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

    def modify_table(self):
        # Modify data in a specific cell
        item = QTableWidgetItem('Updated Value')
        self.table_widget.setItem(0, 1, item)

        # Add a new row with data
        row = self.table_widget.rowCount()
        self.table_widget.insertRow(row)
        new_data = ['New Name', '40', 'Germany']
        for col, value in enumerate(new_data):
            item = QTableWidgetItem(value)
            self.table_widget.setItem(row, col, item)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()

    # Call the modify_table function after some time or based on an event
    window.modify_table()

    app.exec_()
