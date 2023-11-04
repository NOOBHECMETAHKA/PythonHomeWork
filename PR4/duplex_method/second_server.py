# Сервер 1
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8000

client_socket.connect((host, port))
print('Connected to', host, port)

data = client_socket.recv(1024)
print('Received from server:', data.decode())

message = 'Hello, server!'
client_socket.sendall(message.encode())

client_socket.close()

