import select
import socket
import re
import sys
import os
from Class.Robot import Robot
from Class.Carte import Carte
from Class.Maps import Maps

class Serveur():
	"""
	La classe du Serveur
	"""
	def __init__(self, carte, hote="", port=12800):
		"""
		initialise le serveur
		"""

		self.port = port
		self.hote = hote

		self.lstClient = []
		self.lstRobot = []
		self.carte = carte
		self.begin = False
		self.round = 0

		self.reg1 = r'^[nseo]([1-9][0-9]*)?$'
		self.reg2 = r'^[mp][nseo]([1-9][0-9]*)?$'
		print("map choisi :\n{}\n".format(self.carte.__str__()))

		print("setup the connexion ...")
		self.mainConnexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.mainConnexion.bind((hote, port))
		self.mainConnexion.listen(5)

		print("done\n")
		print("listening on port : {}".format(port))

	def __del__(self):
		self.sendMessageToAll("la partie est terminer")
		print("[Serveur] : serveur will close\n")
		for client in self.lstClient:
			try:
				client.send("end".encode())
				client.close()
			except Exception as e:
				print(e)

		print("[Serveur] : all client connexion are now close\n")
		print("[Serveur] : now close main connexion and exit\n")
		self.mainConnexion.close()

	def getClient(self):
		"""
		function qui obtient les client avant le debut de la partie
		"""
		print("\n[Serveur] : now wait form client to connect ...\n")
		while self.begin is False:
			# regarde pour de nouvel connexion
			connexionW, _, _ = select.select([self.mainConnexion], [], [], 0.05)
			self.addClient(connexionW)

			connexionR = []
			try:
				connexionR, _, _ = select.select(self.lstClient, [], [], 0.05)
			except select.error:
				pass
			else:
				for client in  connexionR:
					msgRcv = client.recv(1024)
					msgRcv = msgRcv.decode()
					print("[Serveur] : from client {} : {}".format(self.lstClient.index(client) + 1, msgRcv))
					if msgRcv in "c":
						if self.begin is False:
							self.begin = True
						else:
							client.send("[Serveur] : la partie a deja commencer".encode())
					else:
						self.handleMsg(msgRcv, client)
		print("\n[Serveur] : all client are connected\n")
		self.playGame()

	def readClient(self, connexionRead):
		"""
		function qui lit les messages des clients
		"""
		for client in  connexionRead:
			msgRcv = client.recv(1024)
			msgRcv = msgRcv.decode()
			print("[Serveur] : from client {} : {}".format(self.lstClient.index(client) + 1, msgRcv))
			self.handleMsg(msgRcv, client)

	def addClient(self, connexionWanted):
		"""
		function qui ajoute les clients
		"""
		for conn in connexionWanted:
			connexion, info = conn.accept()
			print("[Serveur] : client connected :", info)
			# ajoute le client a la liste
			self.lstClient.append(connexion)
			# on choisi une zone aleatoire
			x, y = self.carte.pickRandomLocation()
			# on creer le nouveau robot
			newRobot = Robot(x, y, "Robot-{}".format(len(self.lstRobot) + 1))
			# on ajoute le robot a la liste
			self.lstRobot.append(newRobot)
			# on renvoie la map update a tout les clients
			self.reSendMap()
			# on envoie les infos au nouveau client
			msg = "votre robot : " + newRobot.__str__()
			connexion.send(msg.encode())

	def removeClient(self, client):
		"""
		remove the client
		"""
		index = self.lstClient.index(client)
		del self.lstClient[index]
		del self.lstRobot[index]
		print("[Serveur] : Player-{} disconnect".format(index + 1))
		client.close()
		self.reSendMap()
		self.sendMessageToAll("Player-{} quit\n".format(index + 1))
		if len(self.lstClient) > 0:
			if self.round is index and index < len(self.lstClient):
				self.lstClient[index].send("[Serveur] : its your turn\n".encode())
			else:
				self.lstClient[index - 1].send("[Serveur] : its your turn\n".encode())
			if self.round >= index + 1:
				self.round -= 1

	def playGame(self):
		"""
		function qui gere le jeu
		"""
		self.sendMessageToAll("la partie a commencer\n")
		self.sendMessageToAll("au tour du player-{}\n".format(self.round + 1))
		while self.begin is True and len(self.lstClient) > 0:
			self.handleAction()
			self.handleNewConnection()
			connexionR = []
			try:
				connexionR, _, _ = select.select(self.lstClient, [], [], 0.05)
			except select.error:
				pass
			else:
				self.readClient(connexionR)

	def handleAction(self):
		robot = self.lstRobot[self.round]
		if robot.needMovement(self.carte) is False:
			robot.update(self.carte)
			self.reSendMap()
			if self.carte.haveWin(robot.coord) is True:
				self.begin = False
				self.sendMessageToAll("the Player-{} have win".format(self.round + 1))
			else:
				self.round += 1
				if len(self.lstRobot) <= self.round:
					self.round = 0
				self.sendMessageToAll("au tour du player-{}\n".format(self.round + 1))

	def handleNewConnection(self):
		"""
		function qui gere les nouvelles connection quand la partie a commencer
		"""
		connW, _, _ = select.select([self.mainConnexion], [], [], 0.05)
		for c in connW:
			sock, info = c.accept()
			sock.send("[Serveur] : la partie a commencer, bye!\n".encode())
			sock.send("end".encode())
			sock.close()

	def handleMsg(self, msg, client):
		"""
		gere les messages envoyer par les clients
		"""
		av = msg.split(' ')
		if "/say" == av[0]:
			return self.sendMessageFromClientToAll(av, client)
		if "/ls" == av[0]:
			return self.sendListPlayer(client)
		if "/end" == av[0]:
			return self.removeClient(client)
		if re.search(self.reg1, av[0]):
			return self.handleMove(client, av[0])
		if re.search(self.reg2, av[0]):
			return self.handleBuild(client, av[0])
		msg = "[Serveur] : {} command not found".format(msg)
		client.send(msg.encode())

	def handleBuild(self, client, msg):
		"""
		gere le construction
		"""
		if self.checkTurn(client) is False:
			return False
		ttype = msg[0]
		direction, count = self.getDirAndCount(msg[1:])
		index = self.lstClient.index(client)
		msg = "[Serveur] : Build register\n"
		msg += "type      : {}\n".format(ttype)
		msg += "direction : {}\n".format(direction)
		msg += "count     : {}\n".format(count)
		client.send(msg.encode())
		self.checkAction(client, self.lstRobot[index], ttype, direction, count)
		return True

	def handleMove(self, client, msg):
		"""
		gere les mouvements
		"""
		if self.checkTurn(client) is False:
			return False
		index = self.lstClient.index(client)
		robot = self.lstRobot[index]
		direction, count = self.getDirAndCount(msg)
		msg = "[Serveur] : Mouvement register\n"
		msg += "direction : {}\n".format(direction)
		msg += "count     : {}\n".format(count)
		client.send(msg.encode())
		self.checkAction(client, robot, direction, direction, count)
		return True

	def checkTurn(self, client):
		index = self.lstClient.index(client)
		if self.begin is False:
			msg = "[Serveur] : the game is not started yet,\n"
			msg += "press c to begin the game"
			client.send(msg.encode())
			return False
		if index is not self.round:
			msg = "[Serveur] : is not your turn to play,\n"
			msg += "first wait for the Player-{} to play\n".format(self.round + 1)
			client.send(msg.encode())
			return False
		return True

	def getDirAndCount(self, str):
		"""
		function qui recureper la direction et le nombre de coup
		"""
		dire = str[0]
		try:
			if len(str[1:]):
				count = int(str[1:])
			else:
				count = 1
		except Exception as e:
			print("{} : {}".format(e, str[1:]))
			coutn = 1
		return dire, count

	def checkAction(self, client, robot, ttype, direction, count):
		"""
		function qui verifie l'action
		"""
		if self.carte.actionOk(robot.coord, ttype, direction, count) is False:
			client.send("[Serveur] : Erreur mouvement impossible\n".encode())
		else:
			client.send("[Serveur] : Mouvement enregistrer\n".encode())
			robot = robot.setMovement(ttype, direction, count)

	def addRobotToMap(self, main_robot):
		"""
		function qui ajoute le robot a la map
		"""
		save = dict(self.carte.labyrinthe)
		lab = self.carte.labyrinthe
		for robot in self.lstRobot:
			lab[robot.coord] = "x"
		lab[main_robot.coord] = "X"
		chaine = self.carte.__str__()
		self.carte.labyrinthe = save
		return chaine

	def sendListPlayer(self, client):
		"""
		envoie la list des clients connecter
		"""
		msg = "[Serveur] :\n"
		for i, rob in enumerate(self.lstRobot):
			msg += "Player-{} : ".format(i + 1) + rob.__str__() + "\n"
		msg += "\nyou are the Player-{}".format(self.lstClient.index(client) + 1)
		client.send(msg.encode())

	def sendMessageToAll(self, msg):
		"""
		function qui envoie un message a tout les clients
		"""
		msg = "[Serveur] : {}".format(msg)
		msg = msg.encode()
		for client in self.lstClient:
			client.send(msg)

	def sendMessageFromClientToAll(self, av, client):
		"""
		function qui envoie un message a tout les clients
		"""
		msg = ' '.join(av[1:])
		res = "[Serveur] : your msg : {} : have been send".format(msg)
		msg = "[Player-{}] : {}".format(self.lstClient.index(client) + 1, msg)
		msg = msg.encode()
		for c in self.lstClient:
			if c is not client:
				c.send(msg)
		client.send(res.encode())

	def reSendMap(self):
		"""
		function qui renvoie la map a tout les clients
		"""
		for rob, cli in zip(self.lstRobot, self.lstClient):
			msg = self.addRobotToMap(rob)
			cli.send(msg.encode())
