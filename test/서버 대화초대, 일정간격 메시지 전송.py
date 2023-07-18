import socket
import threading
import time


class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 8080))
        self.server_socket.listen(1)

        self.clients = {}  # Dictionary to store connected clients

    def start(self):
        print("Server started. Listening for connections...")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print("Client connected:", client_address, client_socket)

            # Start a new thread for each client
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

            # Start a new thread for each client
            # threading.Thread(target=self.send_messages, args=(client_socket,)).start()

    def send_messages(self, client_socket):
        while True:
            message = "Hello from server!"
            client_socket.send(message.encode('utf-8'))
            time.sleep(5)  # Sends message every 5 seconds

    def handle_client(self, client_socket):
        print('클라이언트 등록')
        client_name = client_socket.recv(1024).decode('utf-8')
        self.clients[client_name] = client_socket
        print(client_name)

        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if data.startswith('/invite'):
                    _, recipient = data.split(' ', 1)
                    if recipient in self.clients:
                        self.send_invitation(client_name, recipient)
                    else:
                        self.send_message(client_socket, "Recipient not found.")
                else:
                    self.broadcast_message(client_name, data)
            except ConnectionResetError:
                break

        # Remove the client on disconnection
        print("Client disconnected:", client_name)
        del self.clients[client_name]

    def send_message(self, client_socket, message):
        client_socket.send(message.encode('utf-8'))

    def broadcast_message(self, sender, message):
        print(sender, message)
        for client_name, client_socket in self.clients.items():
            if client_name != sender:
                self.send_message(client_socket, f"{sender}: {message}")

    def send_invitation(self, sender, recipient):
        message = f"{sender} has invited you to a conversation."
        self.send_message(self.clients[recipient], message)


if __name__ == "__main__":
    server = Server()
    server.start()
