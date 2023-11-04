#   Клиент

import socket

messages = [
    'H',
    'E',
    'L',
    'L',
    'O',
]

for message in messages:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8888))
    client_socket.send(message.encode('utf-8'))
    client_socket.close()

