#   Сервер
import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8888))
server_socket.listen(5)


def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))
    client_socket.close()


while True:
    client_socket, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

