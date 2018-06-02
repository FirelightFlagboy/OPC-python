# -*-coding:utf-8 -*

import os
from pgcd import ft_pgcd

def ft_ppcm(nb1, nb2):
	print(ft_pgcd(nb1, nb2))
	return ((nb1 * nb2) / ft_pgcd(nb1, nb2) if nb2 != 0 else 0)

def main():
	"""fonction principale du programme
	permet de lancer la fonction ppcm avec ces
	deux parametre"""
	error = 0
	ipt = ""
	while len(ipt) < 1 or error == 1:
		error = 0
		ipt = input("saisissez un nb 1:\n>>>")
		try:
			nb1 = int(ipt)
		except Exception as e:
			error = 1
			print ("Error : conversion : ",e)

	ipt = ""
	while len(ipt) < 1 or error == 1:
		error = 0
		ipt = input("saisissez un nb 2:\n>>>")
		try :
			nb2 = int(ipt)
		except Exception as e:
			error = 1
			print("Error : conversion : ",e)
	print("le pgcd de {0} et de {1} donne\n>{2}".format(nb1, nb2, ft_ppcm(nb1, nb2)))
	os.system("pause")

if __name__ == '__main__':
	"""quand le programme est lancer en temps que
	programme principale, il execute alors
	la fonction main()"""
	main()