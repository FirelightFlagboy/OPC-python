import os
import re
from Carte import Carte

def getMapFromDir(directory):
	"""lit dans le repertoire donnée"""

	lstCarte = []
	# on parcoure le dossier
	for nom_fichier in os.listdir(directory):
		# si le fichier se termine par .txt
		if nom_fichier.endswith(".txt"):
			chemin = os.path.join(directory, nom_fichier)
			nom_carte = nom_fichier[:-3].lower()
			# on ouvre le fichier pour le lire
			with open(chemin, "r") as fichier:
				contenu = fichier.read()
				lstCarte.append(Carte(nom_carte,contenu))
	return lstCarte

def displayMenuMap(lstCarte):
	"""
		affiche le menu du choix des cartes
		renvoie si il y a une partie en cours
		ainsi que sont index
	"""
	partieEnCours = False
	index_last_save = -1
	print("Labyrinthes existants :")
	for i, carte in enumerate(lstCarte):
		print("  {} - {}".format(i + 1, carte.nom))
		# si le nom est last_save alors il s'agit d'une partie sauvegarde
		if carte.nom in "last_save.":
			partieEnCours = True
			index_last_save = i+1

	return partieEnCours, index_last_save

def getIndexFromChoice(nbCarte, partieSave, indexParti):
	"""
		function qui demande a l'utilisateur de choisir une carte
	"""
	# Si il y a une partie sauvegardée, on l'affiche
	choix = " "
	if partieSave:
		print("voulez-vous terminer votre derniere partie ?")
		while choix not in "oui" and choix not in "non":
			choix = input("oui/non\n>")
			choix = choix.lower()

	#si le joueur ne veut pas jouer a son ancienne partie ou qu'on en a pas trouver
	if choix not in "oui" :
		ex = r"^[0-9]+$"
		#on tourne tant que le jouer n'a pas saisi une bonne valeur
		while 1:
			print("pour choisir une carte:")
			while re.search(ex,choix) is None:
					choix = input("saisissez un chiffre compris entre 1 et {}\n>".format(nbCarte))
			try:
				choix = int(choix)
				if choix >= 1 and choix <= nbCarte:
					break
				else:
					print("le choix doit etre compris entre 1 et", nbCarte)
			except Exception as e:
				raise print("Erreur: {} : impossible de convertir la valeur choix >{} en int".format(e, choix))
			choix = " "

	#si le joueur veut jouer a son ancienne partie
	else:
		choix = indexParti
		print(choix)
	return choix - 1

def getChoice():
	ex = r"^[neosQq]([1-9][0-9]*)?$"
	print("saisissez une direction (n/e/o/s) ou Q pour quitter:")
	choix = ""
	while re.search(ex, choix) is None:
		choix = input(">")
	return choix

def userWantToPlayAgain():
	choix = " "
	while choix != "oui" and choix != "non":
			choix = input("voulez-vous faire une autre partie ?\noui/non\n>")
			choix = choix.lower()

	return choix in "oui"
