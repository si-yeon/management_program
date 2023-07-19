import json
import threading

from server.controller.controller_common import CommonController
from server.model.chat_dao import ChatDAO
from server.model.manager_dao import ManagerDAO
from server.model.clothes_dao import ClothesDAO
from server.storage.temp_storage import TempStorage


class ClientController(TempStorage, CommonController):
    def __init__(self, name, conn, addr, room):
        self._clientId = 0
        self._clientName = name
        self._clientSocket = conn
        self._clientAddress = addr
        self._currentRoom = room

        self._exists = True

        receiving_thread = threading.Thread(target=self._receive_from_client)
        receiving_thread.start()

    def input_db_text_data(self, message, room_number):
        """
        채팅 내용 기록
        :param message:
        :param room_number:
        :return:
        """


    # 이름을 가져오는 함수
    def get_name(self):
        return self._clientName

    # 각 클라이언트에 데이터를 전송하는 함수
    def send_to_client(self, data: str):
        packet_length = 4096
        if len(data.encode('utf-8')) < packet_length:
            filled_packet = data.ljust(packet_length)
        else:
            filled_packet = data[:packet_length]
        self._clientSocket.send(filled_packet.encode("UTF-8"))


    def send_json_to_client(self, data):
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

    def _receive_from_client(self):
        """
        클라이언트 패킷 신호 수신
        :return:
        """
        try:
            while self._exists:
                packet = self._clientSocket.recv(4096).decode("UTF-8")
                self._parse_packet(packet)
        except Exception as e:
            self._parse_packet(f'disconnect{self.header_split}')
            print(e)

    def _parse_packet(self, parce: str):
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
                self.input_log('회원가입', str(manager_info))
            elif result == 'doubleid':
                self.send_to_client('doubleid' + self.header_split)
        # 로그인
        elif command == 'login':
            manager_info = eval(self.header_split.join(parsed[1:]).strip())
            manager_id = manager_info['id']
            manager_pw = manager_info['pw']
            result = self.checking_login(id=manager_id, pw=manager_pw)
            if result:
                self._clientId, self._clientName = self.get_name_id(id=manager_id)
                self.send_to_client(f'login{self.header_split}{self._clientName}')
                self.input_log('로그인', f'{self._clientName}({self._clientId}) 이/가 로그인하였습니다.')
                self._currentRoom.add_client(self)
            elif result == 'wrongpw':
                print(manager_id, manager_pw)
                del self.clients[-1]
                self.send_to_client('wrongpw' + self.header_split)
            elif result == 'noneid':
                del self.clients[-1]
                self.send_to_client('noneid' + self.header_split)
        # 채팅방 입장
        elif command == 'enter':
            self.send_previous()
            self._currentRoom.send_enter_message(self._clientName)
            print(f"{self._clientName} 이/가 접속 했습니다")
            self.send_product()


        # 메시지
        elif command == 'message':
            message = self.header_split.join(parsed[1:]).strip()
            self._currentRoom.send_message(self._clientName, message)
            self.input_chat(self._clientId, self._clientName, message)
        # 접속종료
        elif command == 'disconnect':
            if self._exists:
                self._exists = False
                self.input_log('로그아웃', f'{self._clientName}이/가 로그아웃하였습니다.')
                print(self._clientName + ' 이/가 접속 종료 하였습니다')
                self.input_log('logout', self._clientName)
                self._clientSocket.close()
                self._currentRoom.remove_client(self)
                self._currentRoom.get_server().remove_client(self)

    def get_name_id(self, **manager):
        """
        사원아이디, 사원이름 가져오기
        :param manager:
        :return:
        """
        dao = ManagerDAO()
        data = dao.get_manager_by_col('id', manager['id'])
        manager_id = data.id.to_string(index=False)
        manager_name = data.name.to_string(index=False)
        dao.close_connection()
        return manager_id, manager_name

    def checking_login(self, **manager):
        """
        로그인 확인
        :param manager: 로그인 정보
        :return:
        """
        dao = ManagerDAO()
        data = dao.get_manager_by_col('id', manager['id'])
        manager_id = data.id.to_string(index=False)
        manager_pw = data.id.to_string(index=False)
        dao.close_connection()
        if manager_id == manager['id'] and manager_pw == manager['pw']:
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
        data = dao.get_manager_by_col('id', manager['id'])
        if len(data) == 0:
            dao.insert_manager(id=[manager['id']], pw=[manager['pw']], name=[manager['name']],
                               depart=[manager['depart']], position=[manager['position']], img=[manager['img']])
            dao.close_connection()
            return 'welcome'
        else:
            dao.close_connection()
            return 'doubleid'

    def enter_send(self):
        """
        접속자 리스트
        :return:
        """
        enter_list = [client._clientName for client in self._currentRoom._occupants]
        sending_enter_list = 'enter' + self.header_split + self.split_1.join(enter_list)
        for client in self._currentRoom._occupants:
            client.send_to_client(sending_enter_list)

    def send_enter_message(self, name):
        msg = 'update' + self.header_split + name + " 이/가 입장 했습니다."
        self.send_update(msg)

    def send_update(self, msg):
        """
        메시지 전송
        :param msg:
        :return:
        """
        for client in self._currentRoom._occupants:
            client.send_to_client(msg)


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

        for data in dict_data:
            json_data = json.dumps(data)
            self.send_json_to_client('log' + self.header_split + json_data)

    def send_product(self):
        """
        상품 정보 보내기
        :return:
        """
        dao = ClothesDAO()
        data = dao.get_all_clothes()
        dao.close_connection()

        dict_data = data.to_dict('records')

        for data in dict_data:
            json_data = json.dumps(data)
            self.send_json_to_client('product' + self.header_split + json_data)



