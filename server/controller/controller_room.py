from server.storage.temp_storage import TempStorage

class RoomController(TempStorage):
    def __init__(self, name, server_):
        self._roomName = name
        self._server = server_
        self._occupants = []

    # 방 퇴장 시 퇴장 메시지 전송
    def out_send(self):
        out_list = []
        for ocuupant in range(len(self._occupants)):
            out_list.append(self._occupants[ocuupant]._clientName)
        sending_out_list = 'out' + self.header_split + TempStorage.split_1.join(out_list)
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

    # 방에 입장할 때 입장 메시지 전송
    def send_enter_message(self, name):
        msg = 'chat' + self.header_split + name + " 이/가 입장 했습니다."
        self.send_update(msg)

    # 방 접속자 리스트에서 클라이언트 제거
    def remove_client(self, c):
        if c in self._occupants:
            self._occupants.remove(c)
        m = "chat" + self.header_split + c._clientName + " 이/가 퇴장 했습니다."
        self.out_send()
        self.send_update(m)

    # 메시지 전송
    def send_message(self, sender, message):
        packet = "message" + self.header_split + sender + ': ' + message
        for o in self._occupants:
            if not o.get_name() == sender:
                o.send_to_client(packet)

    # 단체로 관련 메시지 전송
    def send_update(self, u):
        for o in self._occupants:
            o.send_to_client(u)