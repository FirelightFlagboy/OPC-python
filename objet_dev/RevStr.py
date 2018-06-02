# -*-coding:utf-8 -*

class RevStr(str):
	"""Classe RevStr herite de la classe str
	elle se contente de redefinir la methode
	__iter__, son mode de parcour sera de
	droite à gauche et non l'inverse
	"""

	def __iter__(self):
		"""Cette methode renvoie un iterateur qui
		parcoure la chaine dans le sens inverse de
		celui de 'Str'"""
		return ItRevStr(self)

class ItRevStr:
	"""ItRevStr gére l'iterateur dans le sens opposé"""
	def __init__(self, chaine_a_parcourir):
		"""on se positionne à la fin de la chaine"""
		self.chaine_a_parcourir = chaine_a_parcourir
		self.position = len(chaine_a_parcourir)

	def __next__(self):
		"""Cette methode doit renvoyer l'element suivant
		dans le parcours,
		ou lever l'exception 'StopIteration' si le parcours est fini
		"""
		if self.position == 0:
			raise StopIteration
		self.position -= 1
		return self.chaine_a_parcourir[self.position]

if __name__ == '__main__':
	import os
	
	ma_chaine = RevStr("bonjour")
	print("ma chaine :",ma_chaine)
	for lettre in ma_chaine:
		print(lettre)

	os.system("pause")