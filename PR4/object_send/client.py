import Sam
import socket
import pickle

obj = Sam.Sam("1628", 30)

data = pickle.dumps(obj)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

client_socket.sendall(data)

client_socket.close()

