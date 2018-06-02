# -*-coding:utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import re
import utils

from Carte import Carte
from Labyrinthe import Labyrinthe
#si le joueur souhaite faire plusieur partie à la fois
while 1:
	partieEnCours = False
	nbCarte = 0
	choix =" "
	aGagner = False
	# On charge les cartes existantes
	cartes = utils.getMapFromDir("cartes")
	nbCarte = len(cartes)
	# on affiche le menu
	partieEnCour, index = utils.displayMenuMap(cartes)
	# on demande a l'utilisateur de choisir
	index = utils.getIndexFromChoice(nbCarte, partieEnCour, index)
	lab = Labyrinthe(cartes[index].labyrinthe)

	chemin = os.path.join("cartes","last_save.txt")
	#une fois que le joueur a choisi sa carte,
	#on peut commencer a jouer

	while aGagner == False:
		#on affiche la carte
		print(lab)
		#on demande au joueur les actions a faire
		choix = utils.getChoice()
		#si le jouer ne souhaite pas quitter alors on la continue
		if choix[:1].lower() not in "q":
			#si le joueur a entrer un direction + une valeur
			if len(choix) > 1:
				#on separe la direction et le nb de deplacement a faire
				direction = choix[:1]
				nbRep = choix[1:]
				#on convertie le nb de Rep de type 'str' en 'int'
				try:
					nbRep = int(nbRep)
				except Exception as e:
					print("Erreur: {} : impossible de convertir la valeur nbRep>{}".format(e, nbRep))
					# on mets un nombre de rep par default
					nbRep = 1
				lab.deplacement(direction, nbRep)
			else:
				lab.deplacement(choix)
			#on verifie si le robot se trouve sur la sortie
			aGagner = lab.RobotOnExit()

			#on enregistre le coup
			with open(chemin, "w") as fichier:
				fichier.write(str(lab))

		else :
			#on quitte si le joueur appuye sur 'Q'
			choix = "exit"
			break

		#si le joueur a gagne ou decide de partir
		if aGagner:
			print(lab)
			print("Bravo,vous avez gagné")
			#on supprime le ficher 'last_save.txt' car on n'en a plus besoin
			os.remove(chemin)
	if choix == "exit" or utils.userWantToPlayAgain() is False:
		break

print("a plus ;)")

os.system("pause")
