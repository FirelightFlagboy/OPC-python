class Robot():
	"""
	La classe robot:
		- contient les coordonnées du robot
		- sont identifient
		- ses actions en cours
	"""


	def __init__(self, x, y, identifient):
		# la coordonnée x et y du robot sur la map
		self.coord = (x, y)
		# l'identifient du robot
		self.identifient = identifient
		# sont action en cours, ainsi que la direction et le nombre de fois
		# qu'elle doit ce repeter
		self.action = None
		self.direction = None
		self.remain = 0

		# vecteur de direction
		self._vecteurDirection = {
			"n":(-1, 0),
			"s":( 1, 0),
			"e":( 0, 1),
			"o":( 0,-1)
		}

	def needMovement(self, carte):
		"""
		methode qui renvoie vraie si le robot a besoin de commande de la part de
		l'utilisateur
		"""
		if self.action is None or self.direction is None or self.remain is 0 or\
		carte.actionOk(self.coord, self.action, self.direction, self.remain) is False:
			return True
		return False

	def setMovement(self, action, direction, count):
		"""
		methode qui set la commande saisi par l'utilisateur
		sur le robot
		"""
		self.action = action
		self.direction = direction
		self.remain = count

	def update(self, carte):
		"""
		fonction qui update le robot
		"""

		if carte.actionOk(self.coord, self.action, self.direction) is False:
			self.action = None
			self.direction = None
			self.remain = 0
			return False

		if self.action in "nseo":
			self.move()
		elif self.action in "mp":
			self.build(carte)

		if self.remain <= 0:
			self.action = None
			self.direction = None
			self.remain = 0

		return True

	def move(self):
		"""
		fonction qui deplace le robot
		"""
		xv, yv = self._vecteurDirection[self.direction]
		x, y = self.coord
		x += xv
		y += yv
		self.remain -= 1
		self.coord = x, y

	def build(self, carte):
		"""
		fonction qui modifie la map
		"""
		xv, yv = self._vecteurDirection[self.direction]
		x, y = self.coord
		x += xv
		y += yv
		coord = x, y
		if self.action is "m":
			carte.buildWall(coord)
		else:
			carte.buildDoor(coord)
		self.remain -= 1

	def __str__(self):
		return "<Robot {} {}>".format(self.identifient, self.coord)
