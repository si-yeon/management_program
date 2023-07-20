from socket import *
import threading

from server.controller.controller_client import ClientController as Client
from server.controller.controller_room import RoomController as Room

from server.storage.temp_storage import TempStorage

class ServerController(TempStorage):
    def __init__(self):
        """
        서버 소켓 생성
        """
        self._serverSocket = socket(AF_INET, SOCK_STREAM)
        self._serverPort = self.serverport
        self._max_clients = self.max_clients
        self.main = Room('main', self)
    def start(self):
        """
        서버 시작
        :return:
        """
        self._serverSocket.bind(('', self._serverPort))
        self._serverSocket.listen(16)
        print("Server ready, port : ", self._serverPort)
        listening_thread = threading.Thread(target=self._accept_connections)
        listening_thread.start()

    def end(self):
        """
        서버 종료
        :return:
        """
        self._serverSocket.close()

    def remove_client(self, client):
        """
        클라이언트 삭제
        :param client: 클라이언트 객체
        :return:
        """
        if client in TempStorage.clients:
            TempStorage.clients.remove(client)

    def _server_full(self):
        """
        클라이언트 수 제한
        :return:
        """
        return self._max_clients == len(TempStorage.clients)

    def _accept_connections(self):
        """
        클라이언트 접속 확인
        :return:
        """
        while True:
            if not self._server_full():
                connection_socket, addr = self._serverSocket.accept()
                new_client = Client(f"Client{len(self.clients) + 1}",
                                    connection_socket, addr, self.main)
                # self.clients.append(new_client)
            else:
                connection_socket, addr = self._serverSocket.accept()
                connection_socket.send(("error" + self.header_split + "Server is full").encode("UTF-8"))
                connection_socket.close()

