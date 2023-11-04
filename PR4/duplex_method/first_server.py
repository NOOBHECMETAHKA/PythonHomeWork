# Сервер 2
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8000

server_socket.bind((host, port))

server_socket.listen(1)
print('Server is listening...')

client_socket, client_address = server_socket.accept()
print('Connected by', client_address)

message = 'Hello, client!'
client_socket.sendall(message.encode())

data = client_socket.recv(1024)
print('Received from client:', data.decode())

client_socket.close()
server_socket.close()