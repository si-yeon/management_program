from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Sample data model with people's information
        self.people_data = [
            {"name": "John", "age": 30, "profession": "Engineer"},
            {"name": "Alice", "age": 25, "profession": "Teacher"},
            {"name": "Bob", "age": 35, "profession": "Doctor"}
        ]

        self.initUI()

    def initUI(self):
        self.table_widget = QTableWidget(self)
        self.setCentralWidget(self.table_widget)

        # Define column mapping
        column_map = {
            0: "name",
            1: "age",
            2: "profession"
        }

        # Set the number of rows and columns in the table
        self.table_widget.setRowCount(len(self.people_data))
        self.table_widget.setColumnCount(len(column_map))

        # Set the headers for each column
        self.table_widget.setHorizontalHeaderLabels(column_map.values())

        # Populate the table with data
        for row, person in enumerate(self.people_data):
            for col, field in column_map.items():
                item = QTableWidgetItem(str(person[field]))
                self.table_widget.setItem(row, col, item)

        self.setWindowTitle("Column Mapping Example")
        self.resize(400, 300)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
