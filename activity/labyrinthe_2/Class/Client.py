from threading import Thread, RLock, Event
import socket
import select
import signal
import os
import sys

class ReadInput(Thread):

	def __init__(self, connexion, displayLock):
		""" constructeur du thread
		"""
		Thread.__init__(self)
		self.connexion = connexion
		self.displayLock = displayLock
		self.loop = True

	def run(self):
		""" fonction qui regarde si le socket du serveur a des
		message a lire
		"""
		while self.loop is True:
			# regarde si le server a envoiyer des messages
			msg_from_serveur, _, _ = select.select([self.connexion], [], [], 0.05)

			# pour chaque message
			for msg_serveur in msg_from_serveur:
				# on recurper le message
				msg = msg_serveur.recv(1024)
				msg = msg.decode()
				# si le message est end alors on quitte
				if msg == "end":
					os.kill(os.getpid(), signal.SIGINT)
					break
				else: # sinon on afficher le message
					with self.displayLock:
						print("\n{}".format(msg))
						print(">> ", end='')
						sys.stdout.flush()

	def stop(self):
		""" function a appele lorsque l'on veut mettre fin au thread"""
		self.loop = False
