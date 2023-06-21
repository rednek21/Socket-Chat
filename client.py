import socket
import threading

# Создаем сокет и устанавливаем соединение с сервером
server_address = input("Введите IP адрес сервера: ")
server_port = int(input("Введите порт сервера: "))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_address, server_port))

nickname = input("Введите ваш никнейм: ")
client_socket.send(nickname.encode())

print(f"Подключен к серверу с никнеймом {nickname}.")


def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode().strip()
            print(message)
        except:
            break


def send_messages():
    while True:
        message = input()
        if message.lower() == "bye":
            client_socket.send(message.encode())
            client_socket.close()
            break
        else:
            try:
                client_socket.send(message.encode())
            except OSError as e:
                print("Ошибка отправки сообщения: ", e)
                client_socket.close()
                break


receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
