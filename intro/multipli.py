# -*-coding:utf-8 -*

"""module multipli contenant la fonction table"""
import os

def table(nb, max=10):
	"""Fonction affichant la table de multiplication par nb de
	1 * nb jusqu'à max * nb"""
	i = 0
	while i < (max+1):
		print(">> ",nb," x ",i," = ",nb*i)
		i +=1

# test de la fonction table
if __name__ == "__main__":
	nbr = input("saisissez une valeur a multilplier :\n>>> ")
	mul = input("saisissez la valuer max de la table (-1 sinon):\n>>> ")
	nbr = int(nbr)
	mul = int(mul)
	if mul > 0:
		table(nbr,mul)
	else :
		table(nbr)
	os.system("pause")