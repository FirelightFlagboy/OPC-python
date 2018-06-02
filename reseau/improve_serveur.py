import select
import socket

hote = ""
port = 12800

main_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_connexion.bind((hote, port))
main_connexion.listen(5)

print("listen to port :", port)

serveur_running = True
connected_clients = []
while serveur_running == True:
	# first we check if their is no client that want
	# to connect to the serveur
	# to do so, we listen to the main_connexion
	# and timeout after 50ms
	connexion_wanted, wlist, xlist = select.select([main_connexion],
		[], [], 0.05)

	for connexion in connexion_wanted:
		connexion_client, infos_connexion = connexion.accept()
		# we add the socket to the array
		connected_clients.append(connexion_client)

	client_to_read = []
	try:
		client_to_read, wlist, xlist = select.select(connected_clients,
			[], [], 0.05)
	except select.error:
		pass
	else:
		for client in  client_to_read:
			msg_rcv = client.recv(1024)
			msg_rcv = msg_rcv.decode()
			print("from client", client)
			print(">", msg_rcv)
			client.send(b"message received")
			if msg_rcv == "fin":
				serveur_running = False

print("end of connexions")
for client in connected_clients:
	client.close()

main_connexion.close()
