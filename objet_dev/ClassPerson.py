# -*-coding:utf-8 -*

class Personne: # Définition de notre classe Personne
	"""Classe définissant une personne caractérisée par :
	- son nom
	- son prénom
	- son âge
	- son lieu de résidence"""

	def __init__(self, nom, prenom, age = 33, lieu_residence = "Paris"): # Notre méthode constructeur
		"""on definit les variable principale """
		self.nom = nom
		self.prenom = prenom
		self.age = age
		self.lieu_residence = lieu_residence