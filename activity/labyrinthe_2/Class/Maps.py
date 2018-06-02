import os
import sys
import re
from Class.Carte import Carte


class Maps():
	"""
	classe qui permet de recurpere les maps d'un dossier choisi
	"""

	def __init__(self, *args):
		"""fonction constructeur de la classe
		"""
		# regex pour verifier le contenue de la map
		self.ex_content = r"^[O.\nU ]+$"
		# regex pour verifier le choix de l'utilisateur
		self.ex_choice = r"^[1-9][0-9]+$"
		# on peut preciser plusieur repertoire ou cherche les fichiers maps
		self.dir_to_search = args
		# variable qui contient la liste des maps
		self.maps = []
		# nb de map
		self.nb_carte = -1

	def displayMenu(self):
		"""
		affiche toute les maps trouver raise une erreur si aucun map
		n'a etait trouver
		"""
		# si il n'y a aucune maps alors on quite
		if self.nb_carte <= 0:
			print("no map found", file=sys.stderr)
			sys.exit(1)
		print("Labytinthes existant :")
		for i, carte in enumerate(self.maps):
			print("  {} - {}".format(i + 1, carte.nom))

	def getMapFromChoice(self):
		"""
		demande a l'utilisateur de choisir une map parmi celle qui existe
		"""
		# on affiche le menu de selection
		self.displayMenu()
		choice = ""
		while 1:
			# on demande a l'utilisateur d'entrer un nombre entre 1 et 'nb carte'
			while re.search(self.ex_choice, choice) is None:
				choice = input("saisissez un chiffre entre 1 et {}\n>> ".format(self.nb_carte))
			# on convertie l'input en int et check si le nb est compris entre 1 est 'nb carte'
			try:
				index = int(choice)
				if index >= 1 and index <= self.nb_carte:
					break
				raise ValueError(
					"Erreur le choix doit etre compris entre 1 et {}".format(self.nb_carte), file=sys.stderr)
			except Exception as e:
				print(e)
			choice = ""
		index += -1
		return self.maps[index]

	def isMapContentOk(self, map):
		"""fonction qui verifie si la map contient:
			une sortie
			un espace
		"""
		if re.search(self.ex_content, map) is None:
			return False
		if "U" not in map:
			return False
		if " " not in map:
			return False
		return True

	def searchFormDir(self, directory):
		"""
		fonction qui lit un repertoire et recuper tout les maps compatible
		"""
		# on regarde si le repertoire existe
		if os.path.exists(directory) is False:
			print("{} doesn't exist".format(directory), file=sys.stderr)
			return []
		# on regarde si le repertoire est bien un repertoire
		if os.path.isdir(directory) is False:
			print("{} not a directory".format(directory), file=sys.stderr)
			return []

		maps = []
		# pour chaque file dans le repertoire
		for nameFile in os.listdir(directory):
			# si le nom se termine par un .txt
			if nameFile.endswith(".txt"):
				# on creer le chemin complet
				path = os.path.join(directory, nameFile)
				# on recupere le nom de la map
				nameMap = nameFile[:-4].lower()
				# on lit le fichier
				with open(path, "r") as mapFile:
					content = mapFile.read()
					if self.isMapContentOk(content):
						# on ajoute le carte a la map
						maps.append(Carte(nameMap, content))
		# on renvoie la liste de maps trouver
		return maps

	def readFromListDir(self):
		""" Obtient la liste de carte contenue dans
		la liste de repertoire donnée a la classe lors de sa construction
		"""
		for rep in self.dir_to_search:
			self.maps.extend(self.searchFormDir(rep))
		self.nb_carte = len(self.maps)
