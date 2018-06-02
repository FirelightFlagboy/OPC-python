# -*-coding:utf-8 -*

def aff_list(*liste):
	print("j'ai reçu : {}".format(*liste))


if __name__ == '__main__':
	import os

	inventaire = [
		("pommes",22),
		("poire",26),
		("fraise",40),
		("banane",12),
		("melon",44)
		]

	aff_list(inventaire) #afficher la liste crue

	inventaire = sorted(inventaire, key=lambda student:student[1]) #on trie la liste on fonction du 2° param le nb 

	aff_list(inventaire)

	os.system("pause")