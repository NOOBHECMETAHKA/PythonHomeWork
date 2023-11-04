import socket
import pickle

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(1)
client_socket, address = server_socket.accept()
data = client_socket.recv(4096)
obj = pickle.loads(data)

print("Number:", obj.getNumber())
print("Age:", obj.getAge())

client_socket.close()
server_socket.close()

