import time
import socket
import select
import sys
import signal
import os
from threading import RLock
from Class.Client import ReadInput, SendInput

hote = "localhost"
port = 12800

# connection avec le serveur
client_connexion = None
readinTh = None

display_lock = RLock()

print("=================================================")
print("  welcome")
print("    commande :")
print("      /say [message]  : send message to all player")
print("      /ls             : list all player connected")
print("      /end            : quit the game")
print("")
print("  hote :", hote)
print("  port :", port)
print("=================================================")

def handler_sigint(n, stack):
	"""gere le signal ctrl-c"""
	if readingTh is not None:
		readingTh.stop()
		readingTh.join()
	if client_connexion is not None:
		# envoir la commande pour quite la partie au serveur
		client_connexion.send("/end".encode())
		client_connexion.close()
	sys.exit(0)

signal.signal(signal.SIGINT, handler_sigint)

# on creer le socket
client_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("try to connect to {}".format((hote, port)))
# on se connecte au serveur
client_connexion.connect((hote, port))
print("done\n")

print(client_connexion.recv(1024).decode())

# on lance la classe thread pour lire les messages du serveur
readingTh = ReadInput(client_connexion, display_lock)
# on dit que le thread est en arrire plan
readingTh.daemon = True
# on lance le thread
readingTh.start()

"""
read input from user
"""
print(">> ", end='')
while True:
	msg = input("")
	# on envoie le message au serveur
	client_connexion.send(msg.lower().encode())

# on termine le thread
readingTh.join()
# on ferme la connection
client_connexion.close()
