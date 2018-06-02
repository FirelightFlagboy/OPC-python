# -*-coding:utf-8 -*

import os

def main():
	"""programme principale qui affiche chaque caractere de src"""
	src = input("saisissez un chaine de caractére :\n>>>")
	for c in src :
		print(c)
	os.system("pause")

if __name__ == '__main__':
	"""permet de lancer le programme principale"""
	main()