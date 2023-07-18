import sqlite3
from socket import *
import threading
import atexit
import datetime
import time
import pandas as pd

# 사용할 구분자
header_split = chr(1)
list_split_1 = chr(2)
list_split_2 = chr(3)


# 공유할 인자들
class TempData:
    clients = []
    room_list = []
    maxClients = 10
    serverPort = 5000

    # DB에 서버 로그 저장
    def input_log(self, type_data, nick):
        conn = sqlite3.connect('./DB/server_data.db')
        cur = conn.cursor()
        time_check = datetime.datetime.now()
        log_data = (type_data, nick, time_check)
        cur.execute('insert into serverlog (type, server_log, time) values (?, ? ,?)', log_data)
        conn.commit()
        conn.close()


# 클라이언트 클래스
class Client(TempData):

    def __init__(self, name, conn, addr, room):

        self._clientName = name
        self._clientSocket = conn
        self._clientAddress = addr
        self._currentRoom = room
        self._duel_list = []

        self._exists = True

        receiving_thread = threading.Thread(target=self._receive_from_client)
        receiving_thread.start()

    # 클라이언트 로그인 데이터 기록
    def input_client_login_data(self):
        conn = sqlite3.connect('./DB/server_data.db')
        cur = conn.cursor()
        check_time = datetime.datetime.now()
        client_login_data = (self._clientName, self._clientAddress[0],
                             self._clientAddress[1], 'login', str(check_time), self._currentRoom._roomName)
        cur.execute(
            'insert into client (nick, ip, port, status, time, room_number) values (?, ?, ?, ?, ?, ?)', client_login_data)
        conn.commit()
        conn.close()

    #클라이언트 로그아웃 데이터 기록
    def input_client_logout_data(self):
        conn = sqlite3.connect('./DB/server_data.db')
        cur = conn.cursor()
        check_time = datetime.datetime.now()
        client_logout_data = (self._clientName, self._clientAddress[0],
                              self._clientAddress[1], 'logout', str(check_time))
        cur.execute(
            'insert into client (nick, ip, port, status, time) values (?, ?, ?, ?, ?)', client_logout_data)
        conn.commit()
        conn.close()

    # 채팅 내용 데이터 베이스에 기록
    def input_db_text_data(self, message, room_number):
        conn = sqlite3.connect('./DB/server_data.db')
        cur = conn.cursor()
        content = message
        check_time = datetime.datetime.now()
        text_data = (room_number, self._clientName, content, str(check_time))
        cur.execute('insert into chat (id, nick, content, time) values (?, ?, ?, ?)', text_data)
        conn.commit()
        conn.close()

    # 1:1 채팅 내용 데이터 베이스에 기록
    def input_db_duel_text_data(self, sender, nick, message):
        conn = sqlite3.connect('./DB/server_data.db')
        cur = conn.cursor()
        content = message
        check_time = datetime.datetime.now()
        text_data = (sender, nick, content, str(check_time))
        cur.execute('insert into chat (sender, nick, content, time) values (?, ?, ?, ?)', text_data)
        conn.commit()
        conn.close()

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
        self.send_to_client('change' + header_split + str(room_id))
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
        except:
            self._parse_packet(f'disconnect{header_split}')

    # 받은 데이터에서 헤더를 분류하여 헤더에 따른 명령을 실행하는 함수
    def _parse_packet(self, parce: str):

        parsed = parce.split(header_split)
        command = parsed[0].strip()

        # 메시지
        if command == '_message':
            self._currentRoom.send_message(self._clientName, header_split.join(parsed[1:]).strip())
            self.input_db_text_data(header_split.join(parsed[1:]).strip(), self._currentRoom._roomName)
            self.input_log('message', self._clientName)

        # 방 생성
        elif command == 'make':
            room_name = header_split.join(parsed[1:]).strip()
            room_id = self.make_room(str(parsed[1]))
            self.input_log('make', self._clientName)
            for o in self._currentRoom._occupants:
                o.send_to_client('room' + header_split + f'{room_name}' + list_split_1 + f'{room_id}')

        # 초대
        elif command == 'invite':
            nick = header_split.join(parsed[1:]).strip()
            self._currentRoom.send_duel_invite(self._clientName, nick)
            self.input_log('invite', self._clientName)

        # 거절
        elif command == 'cancel':
            nick = header_split.join(parsed[1:]).strip()
            self._currentRoom.send_duel_cancel(self._clientName, nick)
            self.input_log('deny', self._clientName)

        # 승인
        elif command == 'accept':
            nick = header_split.join(parsed[1:]).strip()
            self._currentRoom.send_duel_accept(nick)

        # 1:1 대화 메시지
        elif command == 'duel':
            group = header_split.join(parsed[1:]).strip().split(list_split_1)
            friend = group[0]
            message = group[1]
            self._currentRoom.send_duel_message(self._clientName, friend, message)
            self.input_db_duel_text_data(self._clientName, friend, message)
            self.input_log('duel_message', self._clientName)

        # 방 이동
        elif command == 'room':
            room_data = parsed[1].split(list_split_1)
            room_id = room_data[0]
            room_name = room_data[1]
            self.set_room(int(room_id), room_name)
            self.input_log('move room', self._clientName)

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
            json_data = eval(header_split.join(parsed[1:]).strip())
            user_id = json_data['id']
            user_pw = json_data['pw']
            if self.checking_login(user_id, user_pw) == 'True':
                self._clientName = self.send_nick(user_id)
                self.send_to_client('login' + header_split + self._clientName)
                self.input_log('login', self._clientName)
                self._currentRoom.add_client(self)
                self.sending_previous(0)
                self.enter_send()
                self._currentRoom.send_enter_message(self._clientName)
                self.send_room_list()
                print(f"{self._clientName} 이/가 접속 했습니다")
                self.send_to_client('change' + header_split + '0')
            elif self.checking_login(user_id, user_pw) == 'wrongpw':
                print(user_id, user_pw)
                del TempData.clients[-1]
                self.send_to_client('wrongpw' + header_split)
            elif self.checking_login(user_id, user_pw) == 'noneid':
                del TempData.clients[-1]
                self.send_to_client('noneid' + header_split)

        # 서버에서 보내는 메시지
        elif command == "update":
            self._currentRoom.send_update(header_split.join(parsed[1:]).strip())

        elif command == '':
            if self._exists:
                self._exists = False
                self._clientSocket.close()
                self._currentRoom.remove_client(self)
                self._currentRoom.get_server().remove_client(self)

        # 회원가입
        elif command == 'join':
            json_data = eval(header_split.join(parsed[1:]).strip())
            user_id = json_data['id']
            user_pw = json_data['pw']
            user_nick = json_data['nick']
            user_manager = json_data['manager']
            user_img = json_data['img_path']
            if self.checking_join(user_id, user_pw, user_nick, user_manager, user_img) == 'welcome':
                self.send_to_client('welcome' + header_split)
                self.input_log('join', user_nick)
            elif self.checking_join(user_id, user_pw, user_nick, user_manager, user_img) == 'doubleid':
                self.send_to_client('doubleid' + header_split)
            elif self.checking_join(user_id, user_pw, user_nick, user_manager, user_img) == 'doublenick':
                self.send_to_client('doublenick' + header_split)

    # 로그인 시 클라이언트에 닉네임 전송
    def send_nick(self, user_id):
        conn = sqlite3.connect('./DB/server_data.db')
        user_nick = pd.read_sql(f'select nick from tb_member where id = "{user_id}"', conn)
        return user_nick.to_string(index=False, header=False)

    # 회원가입시 중복 데이터 확인 후 가입 및 오류 전송
    def checking_join(self, user, password, nick, manager, img):
        conn = sqlite3.connect('./DB/server_data.db')
        cur = conn.cursor()
        user_id = pd.read_sql('select id from tb_member', conn)
        user_nick = pd.read_sql('select pw from tb_member', conn)
        insert_data = (user, password, nick, manager, img)
        if (user not in user_id) and (nick not in user_nick):
            cur.execute('insert into tb_member (id, pw, nick, manager, img_path) values (?, ?, ?, ?, ?)', insert_data)
            conn.commit()
            conn.close()
            return 'welcome'
        elif user in user_id:
            return 'doubleid'
        elif user in user_nick:
            return 'doublenick'

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
        previous_sting = list_split_1.join([list_split_2.join(package) for package in temp_list])
        self.send_to_client('log' + header_split + previous_sting)

    # 로그인 아이디랑 닉네임 확인
    def checking_login(self, user, password):
        conn = sqlite3.connect('./DB/server_data.db')
        user_id = pd.read_sql(f'select id from tb_member where id = "{user}"', conn)
        user_pw = pd.read_sql(f'select pw from tb_member where id = "{user}"', conn)
        if user_id.id.to_string(index=False, header=False) == \
                user and user_pw.pw.to_string(index=False, header=False) == password:
            return 'True'
        elif len(user_id) == 0:
            return 'noneid'
        else:
            return 'wrongpw'


    # 채팅방 리스트 전송
    def send_room_list(self):
        conn = sqlite3.connect("./DB/server_data.db")
        room_data_previous = pd.read_sql('select * from chat_room_list', conn)
        # room_data = room_data_previous.to_string(index=False, header=False)
        room_data_list = []
        for idx, row in room_data_previous.iterrows():
            room_data_list.append([str(row[0]), row[1]])
        package_sting = list_split_1.join([list_split_2.join(package) for package in room_data_list])
        self.send_to_client('room_list' + header_split + package_sting)

    # 채팅방 생성 함수
    def make_room(self, room_name):
        conn = sqlite3.connect('./db/server_data.db')
        cur = conn.cursor()
        cur.execute(f'insert into chat_room_list (name) values ("{room_name}")')
        conn.commit()
        chat_room_list = pd.read_sql('select id from chat_room_list', conn)
        conn.close()
        name_list = []
        for id in chat_room_list.id.values:
            name_list.append(f'room{id}')
        multi_room = MultiChatServer(room_name, chat_room_list.id.iloc[-1])
        return chat_room_list.id.iloc[-1]

    # 입장시 방 멤버 리스트 전송
    def enter_send(self):
        enter_list = []
        len_range = self._currentRoom._occupants
        for z in range(len(len_range)):
            enter_list.append(self._currentRoom._occupants[z]._clientName)
        sending_enter_list = 'enter' + header_split + list_split_1.join(enter_list)
        for o in self._currentRoom._occupants:
            o.send_to_client(sending_enter_list)


# 채팅 방 클래스
class Room:
    def __init__(self, name, server_):
        self._roomName = name
        self._server = server_
        self._occupants = []

    # 방 퇴장 시 퇴장 메시지 전송
    def out_send(self):
        out_list = []
        for z in range(len(self._occupants)):
            out_list.append(self._occupants[z]._clientName)
        sending_out_list = 'out' + header_split + list_split_1.join(out_list)
        for o in self._occupants:
            o.send_to_client(sending_out_list)

    # 서버 소켓 추출
    def get_server(self):
        return self._server

    # 방 이름 추출
    def get_name(self):
        return self._roomName

    # 방 접속자 리스트에 클라이언트 추가
    def add_client(self, c):
        self._occupants.append(c)
        c.input_client_login_data()

    # 방에 입장할 때 입장 메시지 전송
    def send_enter_message(self, name):
        msg = 'update' + header_split + name + " 이/가 입장 했습니다."
        self.send_update(msg)

    # 방 접속자 리스트에서 클라이언트 제거
    def remove_client(self, c):
        if c in self._occupants:
            self._occupants.remove(c)
        m = "update" + header_split + c._clientName + " 이/가 퇴장 했습니다."
        self.out_send()
        self.send_update(m)

    # 메시지 전송
    def send_message(self, sender, _message):
        packet = "_message" + header_split + sender + ': ' + _message
        for o in self._occupants:
            if not o.get_name() == sender:
                o.send_to_client(packet)

    # 1:1 메시지 전송
    def send_duel_message(self, sender, nick, _message):
        packet = "duel" + header_split + sender + ': ' + _message
        for o in self._occupants:
            if o.get_name() == nick:
                o.send_to_client(packet)

    # 1:1 메시지 초대
    def send_duel_invite(self, sender, nick):
        packet = "invite" + header_split + sender
        for o in self._occupants:
            if o.get_name() == nick:
                o.send_to_client(packet)

    # 1:1 초대 승인
    def send_duel_accept(self, nick):
        packet = "accept" + header_split
        for o in self._occupants:
            if o.get_name() == nick:
                o.send_to_client(packet)

    # 1:1
    def send_duel_cancel(self, sender, nick):
        packet = "cancel" + header_split + sender
        for o in self._occupants:
            if o.get_name() == nick:
                o.send_to_client(packet)

    # 단체로 관련 메시지 전송
    def send_update(self, u):
        for o in self._occupants:
            o.send_to_client(u)


# 스레드 서버 구동 클래스
class MultiChatServer(TempData):
    def __init__(self, room_name, room_id):
        self._maxClients = self.maxClients
        self.room_list.clear()
        conn = sqlite3.connect("./DB/server_data.db")
        room_data_previous = pd.read_sql('select * from chat_room_list', conn)
        for idx, row in room_data_previous.iterrows():
            exec(f"self.{row[1]} = Room({row[0]}, self)")
            eval(f"self.room_list.append(self.{row[1]})")
        self._serverSocket = socket(AF_INET, SOCK_STREAM)
        self._serverPort = self.serverPort

    # 스레드 기동
    def start(self):
        self._serverSocket.bind(('', self._serverPort))
        self._serverSocket.listen(16)
        print("Server ready, port : ", self._serverPort)
        listening_thread = threading.Thread(target=self._accept_connections)
        listening_thread.start()

    # 종료
    def end(self):
        try:
            self._serverSocket.close()
        except:
            pass

    # 클라이언트 리스트에서 클라이언트 제거
    def remove_client(self, c):
        if c in TempData.clients:
            TempData.clients.remove(c)
        del c

    # 서버인원 수 확인
    def _server_full(self):
        return self._maxClients == len(TempData.clients)

    # 접속 확인
    def _accept_connections(self):
        while True:
            if not self._server_full():
                connection_socket, addr = self._serverSocket.accept()
                new_client = Client(f"Client{len(TempData.clients) + 1}",
                                    connection_socket, addr, self.lobby)
                TempData.clients.append(new_client)
            else:
                connection_socket, addr = self._serverSocket.accept()
                connection_socket.send(("error" + header_split + "Server is full").encode("UTF-8"))
                connection_socket.close()

if __name__ == "__main__":
    server = MultiChatServer('lobby', 0)
    server.start()
    atexit.register(server.end)
