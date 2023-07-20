import sys
import pandas as pd
# from openpyxl import Workbook
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QWidget

class ApprovalDocument(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.tableWidget = QTableWidget(5, 3)
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Position", "Approval Status"])

        # Create a button to export data to Excel
        export_button = QPushButton("Export to Excel")
        export_button.clicked.connect(self.export_to_excel)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(export_button)
        self.setLayout(layout)

    def export_to_excel(self):
        # Get the data from the QTableWidget
        rows = self.tableWidget.rowCount()
        cols = self.tableWidget.columnCount()
        data = []
        for row in range(rows):
            row_data = []
            for col in range(cols):
                item = self.tableWidget.item(row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")
            data.append(row_data)

        # Create a pandas DataFrame from the data
        df = pd.DataFrame(data, columns=["Name", "Position", "Approval Status"])

        # Save the DataFrame to an Excel file
        file_name = "approval_document.xlsx"
        df.to_excel(file_name, index=False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApprovalDocument()
    window.show()
    sys.exit(app.exec_())
