
"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

	"""Classe représentant un labyrinthe."""

	def __init__(self, lab = {}):
		"""lab contient toute les coordonne de chaque elment de la map"""
		self.grille = {}
		self.grille = lab

		#on cherche la position du robot dans la map
		for pos, val in self.grille.items():
			if val in "X":
				self.robot = pos
			elif val in "U":
				self.exit = pos

	def __repr__(self):
		"""Quand on entre notre objet dans l'interpreteur"""
		colonne = 1
		chaine = ""
		for pos, val in self.grille.items():

			a, b = pos  #on separe les valeur du tuple,
						#'a' simbolise la colonne et 'b' la ligne
			#quand on arrive a une nouvel ligne
			if a != colonne:
				chaine += "\n"
				colonne = a

			#quand on trouve le robot on verifie si il est bien a la bonne position
			if pos == self.robot:
				val = "X"
			if val in "X" and pos != self.robot:
				val = " "

			chaine += val

		return chaine

	def __str__(self):
		""" quand on souhaite afficher la map
		grâce à un print, on retourne juste sur
		la fonction __repr__"""
		return repr(self)

	def deplacement(self, direction, nbRep = 1):
		"""permer le deplacement du robot dans une direction donné"""
		for i in range(nbRep):
			#si la voie est libre, on bouge
			self.canMove(direction)


	def canMove(self,direction):
		"""test si le robot peut se deplacer dans la dite direction"""
		x, y = self.robot
		#si on veut aller vers le nord
		if direction in "n":
			x -= 1
			#si dans la direction souhaite, il n'y as pas de mur
			if self.grille[x, y] is not "O":
				self.robot = (x, y)

		#si on veut aller vers le sud
		elif direction in "s":
			x += 1
			if self.grille[x, y] is not "O":
				self.robot = (x, y)

		#si on veut aller vers l'est
		elif direction in "e":
			y += 1
			if self.grille[x, y] is not "O":
				self.robot = (x, y)

		#si on veut aller vers l'ouest
		elif direction in "o":
			y -= 1
			if self.grille[x, y] is not "O":
				self.robot = (x, y)


	def RobotOnExit(self):
		"""verifie si le robot ce trouve sur la porte de sortie"""
		if self.robot == self.exit:
			return True
		else:
			return False
