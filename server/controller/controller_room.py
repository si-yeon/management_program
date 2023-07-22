from server.storage.temp_storage import TempStorage

class RoomController(TempStorage):
    def __init__(self, name, server_):
        """
        방 속성
        :param name: 방이름
        :param server_: 서버
        """
        self._roomName = name
        self._server = server_
        self._occupants = []

    def get_server(self):
        """
        서버 객체
        :return:
        """
        return self._server

    def get_name(self):
        """
        방 이름
        :return:
        """
        return self._roomName

    def add_client(self, c):
        """
        클라이언트 추가
        :param c: 클라이언트
        :return:
        """
        self._occupants.append(c)

    def send_enter_message(self, name: str):
        """
        입장 메시지 전달
        :param name: 클라이언트 이름
        :return:
        """
        msg = 'chat' + self.header_split + name + " 이/가 입장 했습니다."
        self.send_all(msg)

    def send_message(self, sender: str, message: str):
        """
        전송자를 제외한 나머지 수신자에게 메시지 전송
        :param sender: 전송자
        :param message: 메시지
        :return:
        """
        packet = "message" + self.header_split + sender + ': ' + message
        for o in self._occupants:
            if not o.get_name() == sender:
                o.send_to_client(packet)

    def send_timeline(self, msg: str):
        """
        타임라인 내용 전달
        :param msg: 메시지
        :return:
        """
        packet = "timeline" + self.header_split + msg
        for o in self._occupants:
            o.send_to_client(packet)

    def send_all(self, msg: str):
        """
        단체 메시지 전달
        :param msg: 메시지
        :return:
        """
        for o in self._occupants:
            o.send_to_client(msg)

    def send_json_all(self, msg: str):
        """
        단체 메시지 전달
        :param msg: 메시지
        :return:
        """
        for o in self._occupants:
            o.send_json_to_client(msg)

    def send_out_message(self, name: str):
        """
        퇴장 메시지 전달
        :param name: 클라이언트 이름
        :return:
        """
        msg = 'chat' + self.header_split + name + " 이/가 퇴장 했습니다."
        self.send_all(msg)

    def remove_client(self, c):
        """
        클라이언트 제거
        :param c: 클라이언트
        :return:
        """
        if c in self._occupants:
            self._occupants.remove(c)


