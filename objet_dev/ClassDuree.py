# -*-coding:utf-8 -*

class Duree:
	"""Classe contenant des durées sous la forme d'un nombre de
	minutes
	et de secondes"""
	def __init__(self, minutes=0, secondes=0):
		"""Constructeur de la classe"""
		self.minutes = minutes # Nombre de minutes
		self.secondes = secondes # Nombre de secondes

	def __str__(self):
		"""Affichage un peu plus joli de nos objets"""
		return "{0:02}:{1:02}".format(self.minutes, self.secondes)

	def __add__(self, objet_a_ajouter):
		"""l'obets_a_ajouter est un entier,
		le nombre de seconde"""
		n_duree = Duree()

		n_duree.minutes = self.minutes
		n_duree.secondes = self.secondes

		n_duree.secondes += obet_a_ajouter

		if n_duree.secondes >= 60:
			n_duree.minutes += n_duree.secondes // 60
			n_duree.secondes = n_duree.secondes % 60

		return n_duree

	def __radd__(self, objet_a_ajouter):
		"""Cette méthode est appelée si on écrit 4 + objet et que
		le premier objet (4 dans cet exemple) ne sait pas comment ajouter
		le second. On se contente de rediriger sur __add__"""
		return self + objet_a_ajouter

	def __iadd__(self, objet_a_ajouter):
		"""si l'utilisateur veut ajouter une valeur
		à l'objet directement, ou "objet_a_ajouter"
		est une valeur en seconde"""
		self.secondes += objet_a_ajouter

			if self.secondes >= 60:
				self.minutes += self.secondes // 60
				self.secondes = self.secondes % 60
				
		return self