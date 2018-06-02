import socket
import signal
import sys

def handler(signal, frame):
	client_connect.close()
	sys.exit(0)

hote = "localhost"
port = 12800

client_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the client to the server
client_connect.connect((hote, port))
print("connection etablie avec le serveur sur le port", port)

# set a signal handler
signal.signal(signal.SIGINT, handler)

# recv a msg from the server
# msg_rc = client_connect.recv(1024)
# print("msg from server : ", msg_rc)
# decode = msg_rc.decode()
# print("status :", decode)

msg_to_send = b""
while msg_to_send != b"fin":
	msg_to_send = input("> ")
	msg_to_send = msg_to_send.encode()
	# envoie le message
	res = client_connect.send(msg_to_send)
	msg_rc = client_connect.recv(1024)
	print(res, ">", msg_rc.decode())

# close the connect between the server and the client
print("fermeture de la connexion")
client_connect.close()
