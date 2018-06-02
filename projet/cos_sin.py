# -*-coding:utf-8 -*

import os
import math
from math import ceil,floor

def ft_sin(minpi,maxpi):
	"""permet de trouver toute les valeur de
	sin(x) = y pour tout x appartenant a [minpi, maxpi]"""
	print("sin(pi*a/b) = x?\n")
	a = input("a ?\n>>")
	b = input("b ?\n>>")
	val = math.pi*int(a)/int(b)
	print("[{0}*pi; {1}*pi] : sin(val)={2}".format(minpi/math.pi, maxpi/math.pi,math.sin(val)))

	print("pi*a/4\n")
	i = minpi
	while i<= maxpi:
		vali = int(ceil(math.sin(i)*1000))
		valval = math.sin(val)*1000
		if vali == int(ceil(valval)) or vali == int(floor(valval)):
			print(">{}/4\n".format(i*4/math.pi))
		i += math.pi/4

	print("pi*a/6\n")
	i = minpi
	while i<= maxpi:
		vali = int(ceil(math.sin(i)*1000))
		valval = math.sin(val)*1000
		if vali == int(ceil(valval)) or vali == int(floor(valval)):
			print(">{}/6\n".format(i*6/math.pi))
		i += math.pi/6

def ft_cos(minpi,maxpi):
	"""permet de trouver toute les valeur de
	cos(x) = y pour tout x appartenant a [minpi, maxpi]"""
	print("cos(pi*a/b) = x?\n")
	a = input("a ?\n>>")
	b = input("b ?\n>>")
	val = math.pi*int(a)/int(b)
	print("[{0}*pi; {1}*pi] : cos(val)={2}".format(minpi/math.pi, maxpi/math.pi,math.cos(val)))

	print("pi*a/4\n")
	i = minpi
	while i<= maxpi:
		vali = int(ceil(math.cos(i)*1000))
		valval = math.cos(val)*1000
		if vali == int(ceil(valval)) or vali == int(floor(valval)):
			print(">{}/4\n".format(i*4/math.pi))
		i += math.pi/4

	print("pi*a/6\n")
	i = minpi
	while i<= maxpi:
		vali = int(ceil(math.cos(i)*1000))
		valval = math.cos(val)*1000
		if vali == int(ceil(valval)) or vali == int(floor(valval)):
			print(">{}/6\n".format(i*6/math.pi))
		i += math.pi/6

def ft_strcmp(s1, s2):
	"""fonction qui compare deux chaine de caractere
	et qui renvoie non si identique,
	ou qui renvoie la difference de l'ordre ASCII des
	deux caractere qui differe"""
	i = 0
	len1 = len(s1)
	len2 = len(s2)
	while i < len1 and i < len2 and s1[i] == s2[i]:
		i += 1
	if i >= len1 and i >= len2:
		return 0
	elif i >= len1 :
		return -ord(s2[i])
	elif i>= len2 :
		return ord(s1[i])
	else :
		return ord(s1[i]) - ord(s2[i])

def ft_input(letter="error"):
	"""fonction qui permet de recuperer et de transformer
	l'input que saisi l'utilisateur en un entier"""
	inp = ""
	res = 0
	error = 0
	while len(inp) <= 0 or error == 1:
		error = 0
		inp = input("saisissez {} de pi*a/b\n>>>".format(letter))
		try :
			inp = int(inp)
			res = inp
			inp = str(inp)
		except TypeError as e:
			print("ERROR > conversion : ",e)
			error = 1
	return res


def main():
	"""fonction principale du programme,
	permet d'executer les fonction necessaire
	en fonction de la demande de l'utilisateur"""
	cos_sin = "test"

	while ft_strcmp(cos_sin,"cos") != 0 and ft_strcmp(cos_sin, "sin"):
		cos_sin = input("cos ou sin ?\n>>>")
		cos_sin = cos_sin.lower()

	print("intervalle\nmin :\n")
	a = ft_input("a")
	b = ft_input("b")
	minpi = (a/b)*math.pi
	print("max :\n")
	a = ft_input("a")
	b = ft_input("b")
	maxpi = (a/b)*math.pi

	print("[{0}*pi; {1}*pi]\n".format(minpi/math.pi, maxpi/math.pi))
	if cos_sin in "sin":
		ft_sin(minpi,maxpi)
	elif cos_sin in "cos":
		ft_cos(minpi,maxpi)

if __name__ == '__main__':
	"""partie qui permet de lancer la fonction main()
	du programme tant que l'utilisateur souhaite continuer"""
	bc = "oui"
	while ft_strcmp(bc, "oui") == 0 :
		main()
		while ft_strcmp(bc, "oui") != 0 and ft_strcmp(bc, "non") != 0 :
			bc = input("voulez-vous continuer ? (oui/non)\n>>>")
			bc = bc.lower()
	os.system("pause")