from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Filtering Example")
        self.setGeometry(100, 100, 600, 400)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(['Name', 'Age', 'Country'])
        self.table_widget.setEditTriggers(QTableWidget.NoEditTriggers)

        # Sample data
        self.data = [
            ['John Doe', '25', 'USA'],
            ['Jane Smith', '30', 'Canada'],
            ['David Johnson', '35', 'USA'],
            ['Emma Thompson', '28', 'Australia'],
            ['Michael Lee', '32', 'UK'],
            ['Sophia Chen', '27', 'China'],
        ]

        self.populate_table()

        # Filter line edit
        self.filter_line_edit = QLineEdit()
        self.filter_line_edit.setPlaceholderText("Enter filter text")
        self.filter_line_edit.textChanged.connect(self.filter_table)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.filter_line_edit)
        main_layout.addWidget(self.table_widget)

        # Main widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def populate_table(self):
        self.table_widget.setRowCount(len(self.data))
        for row, row_data in enumerate(self.data):
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(value)
                self.table_widget.setItem(row, col, item)

    def filter_table(self, text):
        for row in range(self.table_widget.rowCount()):
            hidden = all(text.lower() not in self.table_widget.item(row, col).text().lower()
                         for col in range(self.table_widget.columnCount()))
            self.table_widget.setRowHidden(row, hidden)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
