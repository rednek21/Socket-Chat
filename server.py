import json
import socket
import threading


def handle_client(client_socket, client_address):
    print(f"{client_address} присоединился к чату.")
    client_nickname = client_socket.recv(1024).decode().strip()
    print(f"{client_address} выбрал никнейм {client_nickname}.")
    with open('messages.txt', 'r') as file:
        lines = file.readlines()
        last_messages = lines[-10:]
        for message in last_messages:
            client_socket.send((message[:len(message) - 1]).encode())
            client_socket.send('\n'.encode())
    while True:
        message = client_socket.recv(1024).decode().strip()
        if not message:
            break
        print(f"[{client_nickname}]: {message}")
        broadcast_message(f"[{client_nickname}]: {message}", client_socket)
    client_socket.close()
    print(f"{client_address} покинул чат.")


def broadcast_message(message, sender_client):
    clients_copy = clients.copy()
    clients_copy.remove(sender_client)

    for client in clients_copy:
        client.send(message.encode())

    with open('messages.txt', 'a') as file:
        file.write(f"{message}\n")


with open('config.json', 'r') as f:
    config = json.load(f)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((config['ip'], config['port']))
server_socket.listen()
print("Сервер запущен и готов к работе...")

clients = []

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket, client_address)).start()
