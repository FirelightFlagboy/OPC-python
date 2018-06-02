# -*-coding:utf-8 -*

def mon_decorateur(fonction):
	"""Notre décorateur : il va afficher un message avant l'appel
	de la
	fonction définie"""
	def fonction_modifiee():
		"""Fonction que l'on va renvoyer. Il s'agit en fait d'une
		version
		un peu modifiée de notre fonction originellement définie. On se
		contente d'afficher un avertissement avant d'exécuter notre
		fonction
		originellement définie"""
		print("Attention ! On appelle {0}".format(fonction))
		return fonction()
	return fonction_modifiee

@mon_decorateur
def salut():
	print("Salut !")

if __name__ == '__main__':
	import os

	salut()
	os.system("pause")