import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget
import openpyxl

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QTableWidget to Excel")
        self.setGeometry(100, 100, 600, 400)

        # 예제 데이터로 QTableWidget 채우기
        data = [
            ["이름", "직급", "결재 여부"],
            ["김철수", "대리", "서명"],
            ["이영희", "과장", "미결"],
            ["홍길동", "사원", "서명"],
        ]

        self.table_widget = QTableWidget(self)
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(len(data[0]))
        for row, row_data in enumerate(data):
            for col, cell_data in enumerate(row_data):
                self.table_widget.setItem(row, col, QTableWidgetItem(cell_data))

        self.export_button = QPushButton("Excel로 내보내기", self)
        self.export_button.clicked.connect(self.export_to_excel)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.export_button)

        self.setLayout(layout)

    def export_to_excel(self):
        file_name = "결재문서_사인양식.xlsx"
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        for row in range(self.table_widget.rowCount()):
            for col in range(self.table_widget.columnCount()):
                item = self.table_widget.item(row, col)
                if item is not None:
                    sheet.cell(row=row + 1, column=col + 1, value=item.text())

        workbook.save(file_name)
        print(f"{file_name}로 내보내기가 완료되었습니다.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
