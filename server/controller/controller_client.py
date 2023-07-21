import json
import threading

from server.controller.controller_common import CommonController
from server.controller.controller_room import RoomController as Room
from server.model.chat_dao import ChatDAO
from server.model.manager_dao import ManagerDAO
from server.model.product_dao import ProductDAO
from server.model.take_in_dao import TakeInDAO
from server.model.take_out_dao import TakeOutDAO
from server.storage.temp_storage import TempStorage


class ClientController(TempStorage, CommonController):
    def __init__(self, name: str, conn, addr, room: Room):
        self._clientId = 0
        self._clientName = name
        self._clientSocket = conn
        self._clientAddress = addr
        self._currentRoom = room

        self._exists = True

        receiving_thread = threading.Thread(target=self.receive_from_client)
        receiving_thread.start()

    def get_name(self):
        """
        클라이언트 이름 가져오기
        :return:
        """
        return self._clientName

    def get_name_id(self, id: str):
        """
        사원아이디, 사원이름 가져오기
        :param manager:
        :return:
        """
        dao = ManagerDAO()
        data = dao.get_manager_by_col('id', id)
        manager_id = data.id.to_string(index=False)
        manager_name = data.name.to_string(index=False)
        dao.close_connection()
        return manager_id, manager_name

    def checking_login(self, id: str, pw: str):
        """
        로그인 확인
        :param manager: 로그인 정보
        :return:
        """
        dao = ManagerDAO()
        data = dao.get_manager_by_col('id', id)
        manager_id = data.id.to_string(index=False)
        manager_pw = data.pw.to_string(index=False)
        dao.close_connection()
        if manager_id == id and manager_pw == pw:
            return True
        elif len(data) == 0:
            return 'noneid'
        else:
            return 'wrongpw'

    def checking_join(self, manager: dict):
        """
        회원가입 조건 확인
        :param manager:
        :return:
        """
        print(manager)
        dao = ManagerDAO()
        data = dao.get_manager_by_col('id', manager['id'][0])
        if len(data) == 0:
            dao.insert_manager(manager)
            dao.close_connection()
            return 'welcome'
        else:
            dao.close_connection()
            return 'doubleid'

    def send_previous(self):
        """
        이전 채팅기록 보내기
        :return:
        """
        dao = ChatDAO()
        data = dao.get_all_chat()
        dao.close_connection()

        reverse_data = data.iloc[::-1]

        max_fifty_data = reverse_data.iloc[:50]

        dict_data = max_fifty_data.to_dict('records')

        dict_data.reverse()

        for data in dict_data:
            json_data = json.dumps(data)
            self.send_json_to_client('log' + self.header_split + json_data)

    def send_product(self, is_all=False):
        """
        상품 정보 보내기
        :param is_all: True: 모두, False: 접속자만
        :return:
        """
        dao = ProductDAO()
        data = dao.get_all_product()
        dao.close_connection()

        dict_data = data.to_dict('records')

        for idx, data in enumerate(dict_data):
            json_data = json.dumps(data)
            if is_all:
                self._currentRoom.send_json_all('product' + self.header_split + str(idx) + self.split_1 + json_data)
            else:
                self.send_to_client('product' + self.header_split + str(idx) + self.split_1 + json_data)

    def send_to_client(self, data: str):
        packet_length = 4096
        if len(data.encode('utf-8')) < packet_length:
            filled_packet = data.ljust(packet_length)
        else:
            filled_packet = data[:packet_length]
        self._clientSocket.send(filled_packet.encode("UTF-8"))

    def send_json_to_client(self, data: str):
        """
        json 데이터 보내기
        :param data:
        :return:
        """
        packet_length = 4096
        if len(data.encode('utf-8')) < packet_length:
            filled_packet = data.ljust(packet_length)
        else:
            filled_packet = data[:packet_length]
        self._clientSocket.send(bytes(filled_packet, 'utf-8'))

    def receive_from_client(self):
        """
        클라이언트 패킷 신호 수신
        :return:
        """
        try:
            while self._exists:
                packet = self._clientSocket.recv(4096).decode("UTF-8")
                self.parse_packet(packet)
        except Exception as e:
            self.parse_packet(f'disconnect{self.header_split}')
            print(e)

    def parse_packet(self, parce: str):
        """
        전달받은 패킷신호 파싱
        :param parce: 패킷신호
        :return:
        """
        parsed = parce.split(self.header_split)
        # 헤더
        command = parsed[0].strip()
        # 회원가입
        if command == 'join':
            manager_info = eval(self.header_split.join(parsed[1:]).strip())
            result = self.checking_join(manager_info)
            if result == 'welcome':
                self.send_to_client('welcome' + self.header_split)
                self.input_log('회원가입', f"{manager_info['name'][0]}({manager_info['id'][0]})이/가 회원가입 했습니다.")
            elif result == 'doubleid':
                self.send_to_client('doubleid' + self.header_split)
        # 로그인
        elif command == 'login':
            manager_info = eval(self.header_split.join(parsed[1:]).strip())
            manager_id = manager_info['id'][0]
            manager_pw = manager_info['pw'][0]
            result = self.checking_login(manager_id, manager_pw)
            if result:
                self._clientId, self._clientName = self.get_name_id(manager_id)
                self.clients.append(self)
                self._currentRoom.add_client(self)
                self.send_to_client(f'login{self.header_split}{self._clientName}')
                msg = f'{self._clientName}({self._clientId})이/가 로그인 했습니다.'
                self._currentRoom.send_timeline(msg)
                self.input_log('로그인', msg)
            elif result == 'wrongpw':
                del self.clients[-1]
                self.send_to_client('wrongpw' + self.header_split)
            elif result == 'noneid':
                del self.clients[-1]
                self.send_to_client('noneid' + self.header_split)
        # 채팅방 입장
        elif command == 'enter':
            self.send_previous()
            self._currentRoom.send_enter_message(self._clientName)
            self.send_product()
        # 메시지
        elif command == 'message':
            message = self.header_split.join(parsed[1:]).strip()
            self._currentRoom.send_message(self._clientName, message)
            self.input_chat(self._clientId, self._clientName, message)
        # 갱신
        elif command == 'renew':
            self.send_product()
        # 상품 추가
        elif command == 'add':
            product_info = eval(self.header_split.join(parsed[1:]).strip())
            dao = ProductDAO()
            dao.insert_product(product_info)
            dao.close_connection()
            self.send_product(True)
            msg = f"{product_info['name'][0]}[{product_info['code'][0]}]의 정보가 추가되었습니다."
            self._currentRoom.send_timeline(msg)
            self.input_log('상품추가', msg)
        # 상품 수정, 입고, 출고
        elif command == 'modify':
            product_info = eval(self.header_split.join(parsed[1:]).strip())
            dao = ProductDAO()
            dao.update_product(product_info)
            dao.close_connection()
            self.send_product(True)
            msg = f"{product_info['name']}[{product_info['code']}]의 정보가 수정되었습니다."
            self._currentRoom.send_timeline(msg)
            self.input_log('상품수정', msg)
        # 상품 삭제
        elif command == 'delete':
            product_info = eval(self.header_split.join(parsed[1:]).strip())
            dao = ProductDAO()
            dao.delete_product(product_info)
            dao.close_connection()
            self.send_product(True)
            msg = f"{product_info['name']}[{product_info['code']}]의 정보가 삭제되었습니다."
            self._currentRoom.send_timeline(msg)
            self.input_log('상품삭제', msg)
        # 상품 입고
        elif command == 'take_in':
            product_info = eval(self.header_split.join(parsed[1:]).strip())
            dao = TakeInDAO()
            dao.insert_take_in(product_info)
            dao.close_connection()
            msg = f"{product_info['name'][0]}[{product_info['code'][0]}]이/가 {product_info['amount'][0]}개 입고되었습니다."
            self._currentRoom.send_timeline(msg)
            self.input_log('상품입고', msg)
        # 상품 출고
        elif command == 'take_out':
            product_info = eval(self.header_split.join(parsed[1:]).strip())
            dao = TakeOutDAO()
            dao.insert_take_out(product_info)
            dao.close_connection()
            msg = f"{product_info['name'][0]}[{product_info['code'][0]}]이/가 {product_info['amount'][0]}개 출고되었습니다."
            self._currentRoom.send_timeline(msg)
            self.input_log('상품출고', msg)
        # 접속종료
        elif command == 'disconnect':
            if self._exists:
                try:
                    msg = f'{self._clientName}({self._clientId})이/가 로그아웃 했습니다.'
                    self._currentRoom.send_out_message(self._clientName)
                    self._currentRoom.send_timeline(msg)
                    self.input_log('로그아웃', msg)
                except Exception as e:
                    print(e)
                self._exists = False
                self._currentRoom.remove_client(self)
                self._currentRoom.get_server().remove_client(self)
                self._clientSocket.close()
