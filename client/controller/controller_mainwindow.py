import sys
import threading

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QListWidgetItem, QWidget, QHBoxLayout, QLabel, \
    QSpacerItem, QSizePolicy

from client.controller.controller_register import RegisterController
from client.controller.controller_signal import SignalController as Signal
from client.view.view_main import Ui_MainWindow as MainView
from client.storage.temporary_storage import TemporaryStorage

class MainWindowController(QMainWindow, MainView, TemporaryStorage):
    def __init__(self):
        super().__init__()
        self.init_setting()
        self.init_variable()
        self.init_widget()
        self.init_signal()
        self.init_method()

    def init_setting(self):
        """
        생성자 설정
        """
        self.setupUi(self)
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.listeningThread = threading.Thread(target=self.check_server_response, daemon=True)
        self.listeningThread.start()

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
            "inventory": "재고",
            "safety_inventory": "안전재고",
        }

    def init_widget(self):
        """
        생성자 위젯 설정
        """
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(self.column_map.values())

    def init_signal(self):
        """
        생성자 시그널
        """
        # 추가 버튼 클릭
        self.pb_add.clicked.connect(self.show_register_view)

        # 수정 버튼 클릭
        self.pb_update.clicked.connect(self.show_register_view)

        # 삭제 버튼 클릭
        self.pb_delete.clicked.connect(self.delete_product)

        # 입고 버튼 클릭
        self.pb_delete.clicked.connect(self.show_take_view)

        # 출고 버튼 클릭
        self.pb_delete.clicked.connect(self.show_take_view)

        # 채팅 버튼 클릭
        self.pb_chat.clicked.connect(self.show_chat_view)

        # 타임라인 버튼 클릭
        self.pb_timeline.clicked.connect(self.show_timeline_view)

        # 관리자 정보 버튼 클릭
        self.pb_profile.clicked.connect(self.show_profile_view)

        # 메시지 관련
        self.signal.chat_signal.connect(self.add_chat_message)
        self.le_msg.returnPressed.connect(self.send_message)
        self.pb_send.clicked.connect(self.send_message)

        # 상품 정보 업데이트
        self.signal.product_signal.connect(self.data_to_table)

    def init_method(self):
        """
        생성자 함수
        """
        self.send_packet(f'enter{self.header_split}')

    def show_take_view(self):
        """
        입,출고 창 보여주기
        :return:
        """

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
        if not self.is_read:
            self.lb_no_read.setText('0')
            self.is_read = True

    def show_register_view(self):
        """
        등록 화면 보여주기
        :return:
        """
        dlg = RegisterController()
        dlg.exec()

    def add_new_row(self):
        checkbox_item = QTableWidgetItem()
        checkbox_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        checkbox_item.setCheckState(Qt.Unchecked)

        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        for i in range(self.tableWidget.columnCount()):
            if i == 0:
                self.tableWidget.setItem(row_count, i, checkbox_item)
            else:
                self.tableWidget.setItem(row_count, i, QTableWidgetItem(f"New Row, Col {i}"))
        self.tableWidget.resizeColumnsToContents()

    def data_to_table(self, data: dict):
        """
        서버로부터 받은 데이터 테이블 위젯에 넣기
        :param data: list(dict())
        :return:
        """
        # for row, product in enumerate(data):
        for col, (field_eng, field_kor) in enumerate(self.column_map.items()):
            item = QTableWidgetItem(str(data[field_eng]))
            self.table_widget.setItem(row, col, item)

    def add_chat_message(self, msg, who: str):
        """
        :param self:
        :param msg: 메시지
        :param who: server,other,me
        :return:
        """
        item = QListWidgetItem(self.lw_chat_room)
        widget = QWidget()
        self.lw_chat_room.setSpacing(3)

        # --- msg_hbox_layout 생성
        self.msg_hbox_layout = QHBoxLayout()
        self.msg_hbox_layout.setContentsMargins(5, 0, 5, 5)

        # --- msg_label 생성
        self.msg_label = QLabel(msg)
        self.msg_label.setWordWrap(True)

        # --- 상대방 메시지, 내 메시지 분류
        if who == 'server':
            self.msg_label.setStyleSheet("background-color: transparent; border: none; color: black")
            self.msg_label.setAlignment(Qt.AlignCenter)
            self.msg_hbox_layout.addWidget(self.msg_label)
        elif who == 'me':
            self.msg_label.setStyleSheet("background-color: #212529; padding: 5px; border-radius: 10px; color: #fff")
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

    def send_message(self):
        """
        메시지 보내기
        :return:
        """
        get_text = self.le_msg.text()
        if get_text != '':
            self.send_packet(f'message{self.header_split}{get_text}')
            self.signal.chat_signal.emit(get_text, 'me')
            self.le_msg.clear()

    def send_packet(self, p):
        self.info['socket'][0].send(p.encode("UTF-8"))

    def check_server_response(self):
        while self.info['connect'][0]:
            if not self.info['socket'][0] == None:
                try:
                    response = self.info['socket'][0].recv(4096).decode("UTF-8")
                    if len(response.encode('utf8')) <= 4096:
                        self._parse_packet(response)
                except Exception as e:
                    print(e)
                    pass

    def _parse_packet(self, p: str):
        """
        서버로부터 수신한 메시지 분류
        :param p:
        :return:
        """
        parsed = p.split(self.header_split)
        command = parsed[0].strip()
        print(command)
        # 대화
        if command == 'message':
            self.signal.chat_signal.emit(' '.join(parsed[1:]).strip(), 'other')
        # 지난 대화기록
        elif command == 'log':
            data = eval(''.join(parsed[1:]).strip())
            if data['id'] == self.info['id'][0]:
                self.signal.chat_signal.emit(f"{data['id']}: {data['content']}", 'me')
            else:
                self.signal.chat_signal.emit(f"{data['id']}: {data['content']}", 'other')
        elif command == 'product':
            data = eval(''.join(parsed[1:]).strip())
            print(type(data))
            self.signal.product_signal.emit(data)
        # 대화방 접속자 알림
        elif command == 'enter':
            list_client = ';'.join(parsed[1:]).strip().split(self.split_1)
            self.friendlistwidget.friend_list.emit(list_client)
        # 대화방 퇴장 알림
        elif command == 'out':
            list_client = ';'.join(parsed[1:]).strip().split(self.split_1)
            self.friendlistwidget.friend_list.emit(list_client)
        # 타임라인 기록
        elif command == 'update':
            self.signal.chat_signal.emit(' '.join(parsed[1:]).strip(), 'server')
        # 관리자 정보
        elif command == 'managerinfo':
            self.classcenterframe.theSignal.emit(' '.join(parsed[1:]).strip(), False)
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
