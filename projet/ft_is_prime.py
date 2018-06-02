# -*-coding:utf-8 -

import os
import math
import sys

def main():
	error = 1
	while error == 1:
		error = 0
		inp = input("saisissez un chiffre:\n>>>")
		try:
			nb = int(inp)
		except (TypeError, ValueError, AssertionError) as e:
			error = 1
			print("Error :", e)
			continue
	for i in range(2, math.ceil(math.sqrt(nb))+1):
		print(i, nb, sep=":")
		if nb % i == 0 and i != nb:
			print("{} n'est pas nb premier".format(nb))
			return
	print("{} est un nb premier".format(nb))

if __name__ == '__main__':
	c = "p"
	while c != "n":
		c = "p"
		main()
		while c not in "y" and c not in "n":
			c = input("do you want to continue ? (y/n):\n")
