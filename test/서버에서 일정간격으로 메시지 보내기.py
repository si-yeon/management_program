import socket
import threading
import time

def send_messages(client_socket):
    while True:
        message = "Hello from server!"
        client_socket.send(message.encode())
        time.sleep(5)  # Sends message every 5 seconds

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)

    print("Server started. Listening for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print("Client connected:", client_address)

        # Start a new thread for each client
        threading.Thread(target=send_messages, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()
