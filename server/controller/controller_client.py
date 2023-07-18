import sqlite3
import threading

from server.controller.controller_common import CommonController
from server.model.manager_dao import ManagerDAO
from server.storage.temp_storage import TempStorage


class ClientController(TempStorage, CommonController):
    def __init__(self, name, conn, addr):
        self._clientId = 0
        self._clientName = name
        self._clientSocket = conn
        self._clientAddress = addr
        self._exists = True

        receiving_thread = threading.Thread(target=self._receive_from_client)
        receiving_thread.start()

    def input_client_login_data(self):
        """
        클라이언트 로그인 데이터 기록
        :return:
        """
        pass

    def input_client_logout_data(self):
        """
        클라이언트 로그아웃 데이터 기록
        :return:
        """
        pass

    def input_db_text_data(self, message, room_number):
        """
        채팅 내용 기록
        :param message:
        :param room_number:
        :return:
        """

    # 채팅 방을 이동시켜주는 함수
    def set_room(self, room_id, room_name):
        if not self._currentRoom is None:
            self._currentRoom.remove_client(self)
        room = None
        for r in self.room_list:
            if room_id == r._roomName:
                room = r
                break
        self._currentRoom = room
        self._currentRoom.add_client(self)
        self.send_to_client('change' + self.header_split + str(room_id))
        self.sending_previous(room_id)
        self.enter_send()
        self._currentRoom.send_enter_message(self._clientName)

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
        print(data, '!\nsent')

    # 클라이언트에서 데이터를 받는 함수
    def _receive_from_client(self):
        try:
            while self._exists:
                packet = self._clientSocket.recv(4096).decode("UTF-8")
                print('received')
                self._parse_packet(packet)
        except Exception as e:
            print(e)

    def _parse_packet(self, parce: str):
        """
        전달받은 패킷신호 파싱
        :param parce: 패킷신호
        :return:
        """

        parsed = parce.split(self.header_split)
        command = parsed[0].strip()

        # 메시지
        if command == '_message':
            message = self.header_split.join(parsed[1:]).strip()
            self._currentRoom.send_message(self._clientName, message)
            self.input_chat(self._clientId, message)
        # 초대
        elif command == 'invite':
            nick = self.header_split.join(parsed[1:]).strip()
            self._currentRoom.send_duel_invite(self._clientName, nick)
            self.input_log('invite', self._clientName)
        # 거절
        elif command == 'cancel':
            nick = self.header_split.join(parsed[1:]).strip()
            self._currentRoom.send_duel_cancel(self._clientName, nick)
            self.input_log('deny', self._clientName)
        # 승인
        elif command == 'accept':
            nick = self.header_split.join(parsed[1:]).strip()
            self._currentRoom.send_duel_accept(nick)
        # 접속종료
        elif command == 'disconnect':
            if self._exists:
                self._exists = False
                print(self._clientName + ' 이/가 접속 종료 하였습니다')
                self.input_client_logout_data()
                self.input_log('logout', self._clientName)
                self._clientSocket.close()
                self._currentRoom.remove_client(self)
                self._currentRoom.get_server().remove_client(self)
        # 로그인
        elif command == 'login':
            manager_info = eval(self.header_split.join(parsed[1:]).strip())
            manager_id = manager_info['id']
            manager_pw = manager_info['pw']
            result = self.checking_login(id=manager_id, pw=manager_pw)
            if result:
                self._clientId, self._clientName = self.get_name_id(id=manager_id)
                self.send_to_client(f'login{self.header_split}{self._clientId}{self.split_1}{self._clientName}')
                self.input_log('로그인', f'{self._clientName}({self._clientId}) 이/가 로그인하였습니다.')
                # self.sending_previous(0)
                print(f"{self._clientName} 이/가 접속 했습니다")
            elif result == 'wrongpw':
                print(manager_id, manager_pw)
                del self.clients[-1]
                self.send_to_client('wrongpw' + self.header_split)
            elif result == 'noneid':
                del self.clients[-1]
                self.send_to_client('noneid' + self.header_split)
        # 회원가입
        elif command == 'join':
            manager_info = eval(self.header_split.join(parsed[1:]).strip())
            result = self.checking_join(manager_info)
            if result == 'welcome':
                self.send_to_client('welcome' + self.header_split)
                self.input_log('회원가입', str(manager_info))
            elif result == 'doubleid':
                self.send_to_client('doubleid' + self.header_split)
        # 서버에서 보내는 메시지
        elif command == "update":
            self._currentRoom.send_update(self.header_split.join(parsed[1:]).strip())
        elif command == '':
            if self._exists:
                self._exists = False
                self._clientSocket.close()
                self._currentRoom.remove_client(self)
                self._currentRoom.get_server().remove_client(self)


    def get_name_id(self, **manager):
        """
        사원번호, 사원이름 가져오기
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

    # 회원가입시 중복 데이터 확인 후 가입 및 오류 전송
    def checking_join(self, **manager):
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

    # 각 방 이전 채팅기록 전송
    def sending_previous(self, room_number):
        conn = sqlite3.connect('./DB/server_data.db')
        cur = conn.cursor()
        datas = cur.execute(f'select nick, content from chat where id = "{room_number}" order by time desc')
        temp_list = list()
        cnt = 0
        for data in datas:
            temp_list.append(data)
            cnt += 1
            if cnt == 50:
                break
        previous_sting = self.split_1.join([self.split_2.join(package) for package in temp_list])
        self.send_to_client('log' + self.header_split + previous_sting)
