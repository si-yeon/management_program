import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QLineEdit, QWidget

class FilterableTableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.tableWidget = QTableWidget(5, 2)
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Age"])

        # Fill the table with some data
        data = [
            ("Alice", 30),
            ("Bob", 25),
            ("Charlie", 35),
            ("David", 28),
            ("Eve", 22)
        ]
        for row, (name, age) in enumerate(data):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(name))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(age)))

        # Create a line edit for filtering
        self.filterLineEdit = QLineEdit()
        self.filterLineEdit.setPlaceholderText("Enter filter text...")
        self.filterLineEdit.textChanged.connect(self.filter_table)

        layout = QVBoxLayout()
        layout.addWidget(self.filterLineEdit)
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

    def filter_table(self):
        filter_text = self.filterLineEdit.text().strip().lower()

        for row in range(self.tableWidget.rowCount()):
            name_item = self.tableWidget.item(row, 0)
            age_item = self.tableWidget.item(row, 1)
            name = name_item.text().lower()
            age = age_item.text().lower()

            if filter_text in name or filter_text in age:
                self.tableWidget.setRowHidden(row, False)
            else:
                self.tableWidget.setRowHidden(row, True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FilterableTableWidget()
    window.show()
    sys.exit(app.exec_())
