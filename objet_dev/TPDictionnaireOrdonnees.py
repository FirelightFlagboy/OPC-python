# -*-coding:utf-8 -*

class DictionnaireOrdonnee:
	"""une classe qui gère un dictionnaire de façon ordonnée 
	grâce à l'utilisation de 2 liste:
	-une pour les clées
	-une pour les valeurs"""
	def __init__(self, base = {}, **CoupleCleValeur):
		"""creer notre dictionnaire ordonnées
		implemente les valeur transmis en paramètre"""

		self._clee = []
		self._valeur = []
		#on ajoute le dictionnaire au liste
		for cle,valeur in base.items():
			#print(cle,":",valeur)
			cle = str(cle)
			valeur = str(valeur)
			self._clee.append(cle)
			self._valeur.append(valeur)
		#on ajoute les couples au liste
		for cle,valeur in CoupleCleValeur.items():
			#print(cle,":",valeur)
			cle = str(cle)
			valeur = str(valeur)
			self._clee.append(cle)
			self._valeur.append(valeur)

	def __len__(self):
		"""retourne la longuer de notre dictionnaire
		ordonnee"""
		i = p = 0
		while i < len(self._clee):
			i += 1
		while p < len(self._valeur):
			p += 1

		if p == i :
			return i
		else:
			raise("Erreur: nb item differe dans les deux liste\n>clee:{}\n>valeur:{}".format(i,p))
			return -1

	def __repr__(self):
		"""Quand on entre notre objet dans l'interpreteur"""
		chaine = "{}"
		if len(self._clee) != 0:
			i = 0
			position = 1
			while i < len(self._clee):
				clee = str(self._clee[i])
				valeur = str(self._valeur[i])
				#print(clee,valeur)
				ttotal = 6+len(clee)+len(valeur)

				chaine = chaine[:position]+"'"+clee+"': "+valeur+", "+chaine[position+ttotal:]
				position += ttotal
				#print(position,ttotal)
				i += 1

			chaine = chaine[:position-2]+"}"+chaine[position-1:]
			chaine = chaine.strip()
		return chaine

	def __str__(self):
		""" quand on souhaite afficher le dictionnaire
		grâce a un print'), on retourne juste sur la 
		fonction __repr__"""
		return repr(self)

	def __getitem__(self, clee):
		"""Cette méthode spéciale est appelée quand on fait
		objet[clee]
		Elle redirige vers self._valeur[index]"""
		if clee not in self._clee:
			raise KeyError("la clee {} n'existe pas".format(clee))
		else:
			i = 0
			while i < len(self):
				if self._clee[i] in clee:
					return self._valeur[i]


	def __setitem__(self, clee, valeur):
		"""Cette méthode est appelée quand on écrit objet[clee] =
		valeur
		On redirige vers:
		-self._clee.append(clee) et self._valeur.append(valeur)
		si la clee n'est pas deja definit dans le dictionnaire
		-self._valeur[index] = valeur si la clee entrer
		existe deja dans le dicitonnaire"""
		
		#dans un premier temps, on test si la clee existe dans le dictionnaire
		i = 0
		while i < len(self):
			if self._clee[i] in clee:
				self._valeur[i] = valeur
				return "la clee {} à été mis à jour et prend la valeur {}".format(clee,valeur)
			i += 1

		#si on a pas trouvé la clee alors on la rajoute dans le dictionnaire

		self._clee.append(clee)
		self._valeur.append(valeur)

		return "la clee {} à été creer dans le dictionnaire et prend la valeur {}".format(clee,valeur)

	def __contains__(self,clee):
		"""renvoie True si la clee 'clee'
		existe dans le dictionnaire"""
		if self._clee in clee:
			return True
		else:
			return False

	def __delitem__(self,clee):
		"""supprime la clee et sa valeur,
		léve une erreur sinon"""
		if clee not in self._clee:
			raise KeyError("la clee {} n'existe pas".format(clee))
		else:
			indice = self._clee.index(clee)
			del self._clee[indice]
			del self._valeur[indice]

	def __iter__(self):

		return iter(self._clee)

	def __add__(self, autre_dictionnaire):
		"""on renvoie un autre dictionnaire contenent les 2"""
		if type(autre_dictionnaire) is not type(self):
			raise TypeError("le dictionnaire envoyer n'est pas de même type")
		tempsDic = DictionnaireOrdonnee()
		#on commence par notre dictionnaire
		for cle,valeur in self.items():
			tempsDic[cle] = valeur
		#on termine avec le second
		for cle,valeur in autre_dictionnaire.items():
			tempsDic[cle] = valeur

		return tempsDic

	def items(self):
		"""renvoie les clee et les valeur 1 par1 """
		for i,clee in enumerate(self._clee):
			yield clee, self._valeur[i]

	def keys(self):
		"""rencoie les clee 1 par 1"""
		for i,clee in enumerate(self._clee):
			yield clee

	def values(self):
		"""renvoie la liste des valeur"""
		return list(self._valeur)

	def reverse(self):
		"""trie le dictionnaire dans le sens inverse des clees"""
		cle = []
		valeur = []

		for key, values in self.items():
			cle.insert(0, key)
			valeur.insert(0,values)

		self._clee = clee
		self._valeur = valeur

	def sort(self):
		"""trie le dictionnaire dans l'ordre des clees"""
		clee_t = sorted(self._cleee)
		valeur = []

		for clee in clee_t:
			valeur.append[self[clee]]

		self._clee = clee_t
		self._valeur = valeur


if __name__ == '__main__':
	import os

	garage = {"ferrari":15, "lamborginie":20, "onda":"voiture"}
	fruit = DictionnaireOrdonnee()
	voiture = DictionnaireOrdonnee()
	legume = DictionnaireOrdonnee(patate=15, tomate=97, salade=34)
	fruit["pomme"]=27
	fruit["bannane"]=40
	print(legume)
	fruit = fruit + legume
	print(fruit)
	print("nb de patate", legume["patate"])
	for cle in legume:
		print(cle)
	

	os.system("pause")