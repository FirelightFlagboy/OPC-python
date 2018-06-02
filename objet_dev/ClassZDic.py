# -*-coding:utf-8 -*

class ZDic(object):
	"""ZDic, une classe qui emulent un dictionaaire"""
	def __init__(self):
		"""créer la variable :
		_dictionnaire"""
		self._dictionnaire = {}

	def __getitem__(self, index):
		"""renvoie la valeur contenue de l'index envoyer en
		parramètre"""
		return self._dictionnaire[index]

	def __setitem__(self, index, valeur):
		"""effect la valeur "valeur" à l'index du 
		dictionnaire"""
		self._dictionnaire[index] = valeur

	def __delitem__(self,index):
		"""supprime la valeur contenue à l'index
		envoyer en parametre"""
		self._dictionnaire.pop(index)

	def __contains__(self,valeur):
		"""cherche si la valeur envoyer en
		parametre est contenue dans le 
		dictionnaire"""
		if valeur in self._dictionnaire.values():
			return True
		else:
			return False

	def __len__(self):
		"""revoie la taille de l'objet"""
		i = 0
		for cle in self._dictionnaire.keys():
			i += 1
		return i
	