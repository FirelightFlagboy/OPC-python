import socket

hote = ""
port = 12800
# constructor
main_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind port 12800
main_conn.bind((hote, port))
# set max connection to 5
main_conn.listen(5)
print("le serveur écoute sur le port", port)

# wait form a client to connect
client_connect, info_connect = main_conn.accept()

print("client_connect : ", client_connect)
print("info_connect : ", info_connect)

# send a msg to the client
msg = "connection accept"
msg_enc = msg.encode()
res = client_connect.send(msg_enc)
print("byte send : ", res)

msg_rcv = b""
while msg_rcv != b"fin":
	msg_rcv = client_connect.recv(1024)
	print(">", msg_rcv.decode())
	client_connect.send(b"5 / 5")

# close the connection to the client
print("fermeture de la connexion")
client_connect.close()
main_conn.close()
