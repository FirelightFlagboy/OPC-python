# -*-coding:utf-8 -*

import os

def ft_pgcd(nb1, nb2):
	"""fonction qui permet de calculer le pgcd
	de nb1 en fonction de nb2, des nombres envoie
	en parametre"""
	if nb1 % nb2 == 0:
		return (nb2)
	else :
		return ft_pgcd(nb2, nb1 % nb2)

def main():
	"""fonction principale du programme
	permet de lancer la fonction pgcd avec ces
	deux parametre"""
	error = 0
	ipt = ""
	while len(ipt) < 1 or error == 1:
		error = 0
		ipt = input("saisissez un nb :\n>>>")
		try:
			nb1 = int(ipt)
		except Exception as e:
			error = 1
			print ("Error : conversion : ",e)

	ipt = ""
	while len(ipt) < 1 or error == 1:
		error = 0
		ipt = input("saisissez un nb != 0:\n>>>")
		try :
			nb2 = int(ipt)
			assert nb2 != 0
		except Exception as e:
			error = 1
			print("Error : conversion : ",e)
		except AssertionError:
			error = 1
			print("Error : le nb doit etre different de 0 !")
	print("le pgcd de {0} et de {1} donne\n>{2}".format(nb1, nb2, ft_pgcd(nb1, nb2)))
	os.system("pause")

if __name__ == '__main__':
	"""quand le programme est lancer en temps que
	programme principale, il execute alors
	la fonction main()"""
	main()