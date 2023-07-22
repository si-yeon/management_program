import json
import os
import sys
import threading
import time
from datetime import datetime

import openpyxl
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QListWidgetItem, QWidget, QHBoxLayout, QLabel, \
    QSpacerItem, QSizePolicy, QPushButton

from client.controller.controller_check import CheckDialog
from client.controller.controller_common import CommonController
from client.controller.controller_name import NameDialog
from client.controller.controller_register import RegisterDialog
from client.controller.controller_signal import SignalController as Signal
from client.controller.controller_take import TakeDialog
from client.storage.temporary_storage import TemporaryStorage
from client.view.view_main import Ui_MainWindow as MainView

class CircleButton(QPushButton):
    # 테두리기 동그란 버튼
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

        self.setGeometry(25, 0, 30, 30)

        # Customize the button's appearance
        self.setStyleSheet("""
            QPushButton {
                 color: #fff;
                 font-size: 15px;
                 border: 1px solid red;
                 border-radius: 15px;
                 font-weight: 1000;
                text-align: center;
                background: red;
            }
        """)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)

class Check(QThread):
    checked = pyqtSignal()

    def run(self):
        while True:
            time.sleep(10)
            self.checked.emit()

class MainWindowController(QMainWindow, MainView, CommonController, TemporaryStorage):
    def __init__(self):
        super().__init__()
        self.init_setting()
        self.init_variable()
        self.init_widget()
        self.init_signal()
        self.init_method()
        self.init_thread()

    def init_setting(self):
        """
        생성자 설정
        """
        self.setupUi(self)
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)

    def init_variable(self):
        """
        생성자 변수 선언 및 초기화
        """
        self.signal = Signal()
        self.is_read = True
        self.column_map = {
            "img": "이미지",
            "code": "코드",
            "type": "분류",
            "brand": "브랜드",
            "name": "상품명",
            "purchase_unit_price": "구매단가",
            "sales_unit_price": "판매단가",
            "safety_inventory": "안전재고",
            "inventory": "재고"}
        self.alarm_flag = True

    def init_widget(self):
        """
        생성자 위젯 설정
        """
        self.pb_chat.setIcon(QIcon('../img/icon/chat.png'))
        self.pb_timeline.setIcon(QIcon('../img/icon/time.png'))
        self.pb_profile.setIcon(QIcon('../img/icon/profile.png'))
        self.pb_logout.setIcon(QIcon('../img/icon/logout.png'))
        self.pb_find.setIcon(QIcon('../img/icon/search.png'))
        self.pb_excel.setIcon(QIcon('../img/icon/excel.png'))
        self.pb_alarm.setIcon(QIcon('../img/icon/alarm.png'))
        self.pb_send.setIcon(QIcon('../img/icon/send.png'))
        self.read_label = CircleButton('0', self.pb_chat)

        self.tableWidget.setColumnCount(len(self.column_map))
        self.tableWidget.setHorizontalHeaderLabels(self.column_map.values())

    def init_signal(self):
        """
        생성자 시그널
        """
        # 엑셀
        self.pb_excel.clicked.connect(self.export_to_excel)

        # 재고부족
        self.pb_shortage_check.clicked.connect(self.show_shortage_inven)

        # 업데이트
        self.pb_inven_check.clicked.connect(lambda x: self.send_packet('renew' + self.header_split))

        # 검색
        self.le_find.returnPressed.connect(self.filter_table)
        self.pb_find.clicked.connect(self.filter_table)

        # 상품 정보
        self.signal.product_signal.connect(self.data_to_table)

        # 추가 버튼 클릭
        self.pb_add.clicked.connect(lambda x=None, txt='추가': self.show_register_view(txt))

        # 수정 버튼 클릭
        self.pb_update.clicked.connect(lambda x=None, txt='수정': self.show_register_view(txt))

        # 삭제 버튼 클릭(txt
        self.pb_delete.clicked.connect(self.delete_product)

        # 입고 버튼 클릭
        self.pb_take_In.clicked.connect(lambda x=None, txt='입고': self.show_take_view(txt))

        # 출고 버튼 클릭
        self.pb_take_out.clicked.connect(lambda x=None, txt='출고': self.show_take_view(txt))

        # 알람 버튼 클릭
        self.pb_alarm.clicked.connect(self.alarm_on_off)

        # 채팅 버튼 클릭
        self.pb_chat.clicked.connect(self.show_chat_view)

        # 메시지 관련
        self.signal.chat_signal.connect(self.add_chat_message)
        self.le_msg.returnPressed.connect(self.send_message)
        self.pb_send.clicked.connect(self.send_message)

        # 타임라인 버튼 클릭
        self.pb_timeline.clicked.connect(self.show_timeline_view)
        self.signal.timeline_siganl.connect(self.add_timeline_message)

        # 관리자 정보
        self.pb_profile.clicked.connect(self.show_profile_view)
        self.signal.manager_signal.connect(self.set_manager_info)

        # 로그아웃
        self.pb_logout.clicked.connect(self.restart_program)

    def init_method(self):
        """
        생성자 함수
        """
        self.send_packet(f'enter{self.header_split}')

    def init_thread(self):
        self.listening_thread = threading.Thread(target=self.check_server_response, daemon=True)
        self.listening_thread.start()

        self.check_thread = Check()
        self.check_thread.checked.connect(self.alarm_shortage_inven)
        self.check_thread.start()

    def restart_program(self):
        self.send_packet(f'disconnect{self.header_split}')
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def alarm_on_off(self):
        """
        알람 켜기/끄기
        :return:
        """
        if self.alarm_flag:
            self.alarm_flag = False
            self.pb_alarm.setIcon(QIcon('../img/icon/alarmoff.png'))
        else:
            self.alarm_flag = True
            self.pb_alarm.setIcon(QIcon('../img/icon/alarm.png'))

    def export_to_excel(self):
        dlg = NameDialog()
        dlg.exec()

        if dlg.is_check:
            file_name = dlg.file_name
            file_path = f'../excel/{file_name}.xlsx'
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            for row in range(self.tableWidget.rowCount()):
                for col in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, col)
                    if item is not None:
                        sheet.cell(row=row + 1, column=col + 1, value=item.text())

            workbook.save(file_path)

    def filter_table(self):
        """
        테이블 검색
        :return:
        """
        filter_text = self.le_find.text().strip().lower()

        for row in range(self.tableWidget.rowCount()):
            code_item = self.tableWidget.item(row, 1)
            type_item = self.tableWidget.item(row, 2)
            brand_item = self.tableWidget.item(row, 3)
            name_item = self.tableWidget.item(row, 4)
            code = code_item.text().lower()
            type = type_item.text().lower()
            brand = brand_item.text().lower()
            name = name_item.text().lower()

            find_list = code + type + brand + name

            if filter_text in find_list:
                self.tableWidget.setRowHidden(row, False)
            else:
                self.tableWidget.setRowHidden(row, True)

    def show_shortage_inven(self):
        """
        재고가 부족한 상품 보여주기
        :return:
        """
        for row in range(self.tableWidget.rowCount()):
            safety_inven_item = self.tableWidget.item(row, 7).text()  # 안전재고
            inventory_item = self.tableWidget.item(row, 8).text()  # 재고

            if int(inventory_item) < int(safety_inven_item):
                self.tableWidget.setRowHidden(row, False)
            else:
                self.tableWidget.setRowHidden(row, True)

    def alarm_shortage_inven(self):
        """
        안전재고보다 재고가 부족한 상품 알림
        :return:
        """
        if self.alarm_flag:
            for row in range(self.tableWidget.rowCount()):
                safety_inven_item = self.tableWidget.item(row, 7).text()  # 안전재고
                inventory_item = self.tableWidget.item(row, 8).text()  # 재고

                if int(inventory_item) < int(safety_inven_item):
                    self.pb_shortage_check.setIcon(QIcon('../img/icon/alarm2.png'))
                    break
            dlg_check = CheckDialog('재고가 부족한 상품이 있습니다.')
            dlg_check.exec()

    def show_take_view(self, action: str):
        """
        입,출고 창 보여주기
        :return:
        """
        row_data = self.get_selected_row_data()
        if len(row_data) > 0:
            dlg = TakeDialog(row_data['code'])
            dlg.exec()
            if dlg.is_check:
                code = row_data['code']
                name = row_data['name']
                inventory = row_data['inventory']
                amount = dlg.sb_num.text()
                time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                if action == '입고':
                    result = int(inventory) + int(amount)
                    row_data['inventory'] = str(result)
                    take_info = {'code': [code], 'name': [name], 'amount': [amount], 'time': [time]}
                    json_data = json.dumps(take_info)
                    msg = f'take_in{self.header_split}{json_data}'
                    self.send_json_packet(msg)
                else:
                    result = int(inventory) - int(amount)
                    if result >= 0:
                        row_data['inventory'] = str(result)
                        take_info = {'code': [code], 'name': [name], 'amount': [amount], 'time': [time]}
                        json_data = json.dumps(take_info)
                        msg = f'take_out{self.header_split}{json_data}'
                        self.send_json_packet(msg)
                    else:
                        check_dlg = CheckDialog('출고할 재고가 부족합니다.')
                        check_dlg.exec()
                json_data = json.dumps(row_data)
                msg = f'modify{self.header_split}{json_data}'
                self.send_json_packet(msg)
        else:
            check_dlg = CheckDialog('상품을 먼저 선택해주세요!')
            check_dlg.exec()

    def show_timeline_view(self):
        """
        타임라인 보여주기
        :return:
        """
        self.stack_view.setCurrentWidget(self.page_timeline)
        self.is_read = False

    def show_profile_view(self):
        """
        관리자 정보 보여주기
        :return:
        """
        self.stack_view.setCurrentWidget(self.page_profile)
        self.is_read = False

    def show_chat_view(self):
        """
        채팅 보여주기
        :return:
        """
        self.stack_view.setCurrentWidget(self.page_chat)
        self.is_read = True
        self.read_label.setText('0')
        last_row_index = self.lw_chat_room.count() - 1
        self.lw_chat_room.setCurrentRow(last_row_index)

    def show_register_view(self, action: str):
        """
        등록 화면 보여주기
        :return:
        """
        if action == '수정':
            row_data = self.get_selected_row_data()
            print(row_data)
            if len(row_data) > 0:
                dlg = RegisterDialog(row_data)
                dlg.code.setDisabled(True)
                dlg.exec()
                if dlg.is_save:
                    json_data = json.dumps(dlg.row_data)
                    msg = f'modify{self.header_split}{json_data}'
                    self.send_json_packet(msg)
            else:
                check_dlg = CheckDialog('수정할 상품을 먼저 선택해주세요!')
                check_dlg.exec()
        else:
            dlg = RegisterDialog()
            dlg.reset_all()
            dlg.exec()
            dict_data = {}
            if len(dlg.row_data) > 0:
                dlg.row_data['add_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                for k, v in dlg.row_data.items():
                    dict_data[k] = [v]
                if dlg.is_save:
                    json_data = json.dumps(dict_data)
                    msg = f'add{self.header_split}{json_data}'
                    self.send_json_packet(msg)

    def set_manager_info(self, info: dict):
        """
        관리자 정보 세팅
        :param info: 관리자 정보
        :return:
        """
        pixmap = QPixmap(info['img'])
        self.lb_img.setPixmap(pixmap)
        self.lb_img.setScaledContents(True)
        self.lb_id.setText(info['id'])
        self.lb_date.setText(info['date'])
        self.lb_name.setText(info['name'])
        self.lb_depart.setText(info['depart'])
        self.lb_position.setText(info['position'])

    def get_selected_row_data(self):
        selected_rows = set(index.row() for index in self.tableWidget.selectedIndexes())
        row_data = {}
        data = []
        if selected_rows:
            for row in selected_rows:
                for col in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, col)
                    data.append(item.text() if item else "")
            row_data = dict(zip(self.column_map.keys(), data))
        return row_data

    def clear_all_rows(self):
        num_rows = self.tableWidget.rowCount()

        for row in reversed(range(num_rows)):
            self.tableWidget.removeRow(row)

    def data_to_table(self, data: dict):
        """
        서버로부터 받은 데이터 테이블 위젯에 넣기
        :param data: list(dict())
        :return:
        """
        row = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row + 1)
        for col, (field_eng, field_kor) in enumerate(self.column_map.items()):
            if field_eng == 'img':
                pixmap = QPixmap(str(data[field_eng])).scaled(100, 100)  # 이미지 크기 조절
                icon = QIcon(pixmap)
                item = QTableWidgetItem()
                item.setIcon(icon)
                item.setTextAlignment(Qt.AlignCenter)

            else:
                item = QTableWidgetItem(str(data[field_eng]))
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(row, col, item)
        self.tableWidget.resizeColumnsToContents()

    def add_timeline_message(self, msg: str, time: str):
        """
        타임라인 메시지
        :param self:
        :param msg: 메시지
        :param who: server,other,me
        :return:
        """
        self.lw_time_line.addItem(msg)
        self.lw_time_line.addItem(time)
        last_row_index = self.lw_time_line.count() - 1
        self.lw_time_line.setCurrentRow(last_row_index)

    def add_chat_message(self, msg: str, who: str):
        """
        :param self:
        :param msg: 메시지
        :param who: server,other,me
        :return:
        """
        # 안 읽은 메시지 표시
        if self.is_read:
            self.read_label.setText('0')
        else:
            num = int(self.read_label.text())
            num += 1
            if num > 99:
                num = 99
            self.read_label.setText(str(num))

        item = QListWidgetItem(self.lw_chat_room)
        widget = QWidget()
        self.lw_chat_room.setSpacing(3)

        self.msg_hbox_layout = QHBoxLayout()
        self.msg_hbox_layout.setContentsMargins(5, 0, 5, 5)

        self.msg_label = QLabel(msg)
        self.msg_label.setWordWrap(True)

        if who == 'server':
            self.msg_label.setStyleSheet("background-color: transparent; border: none; color: black")
            self.msg_label.setAlignment(Qt.AlignCenter)
            self.msg_hbox_layout.addWidget(self.msg_label)
        elif who == 'me':
            self.msg_label.setStyleSheet("background-color: #164DCA; padding: 5px; border-radius: 10px; color: #fff")
            self.msg_hbox_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
            self.msg_hbox_layout.addWidget(self.msg_label)
        elif who == 'other':
            self.msg_label.setStyleSheet("background-color: #D9D9D9; padding: 5px; border-radius: 10px;")
            self.msg_hbox_layout.addWidget(self.msg_label)
            self.msg_hbox_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        widget.setLayout(self.msg_hbox_layout)
        item.setSizeHint(widget.sizeHint())
        self.lw_chat_room.setWordWrap(True)
        self.lw_chat_room.setItemWidget(item, widget)
        self.lw_chat_room.addItem(item)
        self.lw_chat_room.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # 스크롤 최하단에 위치
        scrollbar = self.lw_chat_room.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def delete_product(self):
        """
        선택한 상품 삭제
        :return:
        """
        row_data = self.get_selected_row_data()
        if len(row_data) > 0:
            check_dlg = CheckDialog(f"{row_data['name']}[{row_data['code']}]을/를 정말 삭제하시겠습니까?")
            check_dlg.exec()
            if check_dlg.is_check:
                json_data = json.dumps(row_data)
                msg = f'delete{self.header_split}{json_data}'
                self.send_json_packet(msg)
        else:
            check_dlg = CheckDialog('삭제할 상품을 먼저 선택해주세요!')
            check_dlg.exec()

    def send_message(self):
        """
        메시지 보내기
        :return:
        """
        get_text = self.le_msg.text()
        if get_text != '':
            self.send_packet(f'message{self.header_split}{get_text}')
            self.signal.chat_signal.emit(f'{self.info["name"][0]}: {get_text}', 'me')
            last_row_index = self.lw_chat_room.count() - 1
            self.lw_chat_room.setCurrentRow(last_row_index)
            self.le_msg.clear()

    def check_server_response(self):
        while self.info['connect'][0]:
            if not self.info['socket'][0] == None:
                # try:
                response = self.info['socket'][0].recv(4096).decode("UTF-8")
                if len(response.encode('utf8')) <= 4096:
                    self.parse_packet(response)
                # except Exception as e:
                #     print(e)
                #     pass

    def parse_packet(self, p: str):
        """
        서버로부터 수신한 메시지 분류
        :param p:
        :return:
        """
        parsed = p.split(self.header_split)
        command = parsed[0].strip()
        # 대화
        if command == 'message':
            self.signal.chat_signal.emit(self.header_split.join(parsed[1:]).strip(), 'other')
        # 지난 대화기록
        elif command == 'log':
            data = eval(self.header_split.join(parsed[1:]).strip())
            if data['id'] == self.info['id'][0]:
                self.signal.chat_signal.emit(f"{data['name']}: {data['content']}", 'me')
            else:
                self.signal.chat_signal.emit(f"{data['name']}: {data['content']}", 'other')
        # 상품 정보
        elif command == 'product':
            datas = self.header_split.join(parsed[1:]).strip()
            idx = datas.split(self.split_1)[0]
            data = eval(datas.split(self.split_1)[1])
            if idx == '0':
                self.clear_all_rows()
            self.signal.product_signal.emit(data)
        # 대화방 접속자 알림
        elif command == 'enter':
            list_client = ';'.join(parsed[1:]).strip().split(self.split_1)
            self.friendlistwidget.friend_list.emit(list_client)
        # 대화방 퇴장 알림
        elif command == 'out':
            list_client = ';'.join(parsed[1:]).strip().split(self.split_1)
            self.friendlistwidget.friend_list.emit(list_client)
        # 서버 to 채팅
        elif command == 'chat':
            self.signal.chat_signal.emit(self.header_split.join(parsed[1:]).strip(), 'server')
        # 서버 to 타임라인
        elif command == 'timeline':
            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.signal.timeline_siganl.emit(self.header_split.join(parsed[1:]).strip(), time)
        # 관리자 정보
        elif command == 'manager':
            data = eval(self.header_split.join(parsed[1:]).strip())
            self.signal.manager_signal.emit(data)
        # 연결 종료
        elif command == 'disconnect':
            self.info['socket'][0].close()
            self.info['socket'][0] = None
            self.info['connect'] = False

    def closeEvent(self, e):
        """
        종료 이벤트
        :param e:
        :return:
        """
        self.send_packet(f'disconnect{self.header_split}')
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = MainWindowController()
    a.show()
    sys.exit(app.exec_())
