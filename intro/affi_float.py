# -*-coding:utf-8 -*

def afficher_flottant(flot):
	flot = str(flot)
	pos_p = flot.index(".")
	if pos_p == -1:
		print("ERREUR:impossible de trouver la virgule")
		return -1

	flot = flot.replace(".",",")
	
	return flot[:(pos_p+4)]

if __name__ == "__main__":
	import os

	flot = input("saisissez un flottant :\n>>> ")
	fflot = afficher_flottant(flot)
	if fflot != -1:
		print("le flottant >{0} une fois traité donne >{1}".format(flot,fflot))
	else:
		print("impossible de traiter le flottant")

	os.system("pause")
