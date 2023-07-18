import socket, threading


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))
nickname = input("Choose your nickname: ")


def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break


def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))


# 멀티 클라이언트용 쓰레드
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# 메시지 보내기
write_thread = threading.Thread(target=write)
write_thread.start()