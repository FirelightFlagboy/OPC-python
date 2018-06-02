# -*-coding:utf-8 -*

import os
from donnees import *
from fonction import *

def main():
	lp = get_life()
	fmot =	get_nameFileListeMot()
	fscore = get_nameFileScore()

	name = set_name(fmot)
	#print(name)
	cnam = set_cname(name)

	while lp >0:
		print("il vous reste {} vie".format(lp))
		print(">",cnam)
		l = get_letter()
		bol , cnam = isLetterInName(l,name,cnam)

		if bol:
			print("Bravo tu as trouver une bonne lettre")
		else:
			lp -= 1
			print("la lettre {} n'existe pas dans le mot".format(l))

		if test_fin(name,cnam):
			print("bravo, tu as gagne\ntu as trouvé le mot",name)
			break

	if lp < 1:
		print("dommage, le mot a trouver etait",name)
	else:
		print("tu as gagné un score de {} point".format(lp))
		name = input("saisissez vous nom pour le score\n>")
		print_score(fscore,name,lp)
	os.system("pause")

if __name__ == '__main__':
	main()