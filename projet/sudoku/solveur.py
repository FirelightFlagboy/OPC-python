# -*-coding:utf-8 -*

from math import ceil
from ft_file import *
from donnes import *

nb_sol = 0

def ft_add_glob():
	global nb_sol
	nb_sol += 1

def ft_get_tab(content):
	"""permet d'obtenir un tableau a 2 dimensions"""
	i = 0
	ls = []
	for y in range(0, 9):
		ls.append([])
		for a in range(0, 9):
			if ord(content[i]) >= ord("0") and ord(content[i]) <= ord("9"):
				ls[y].append(ord(content[i]) - ord("0"))
			elif content[i] in "X":
				ls[y].append(0)
			i += 1
		i += 1
	return ls


def ft_first_check(tab):
	"""check le tab obtenue pour la premiére fois"""
	for line in range(0, 9):
		for row in range(0, 9):
			#le 0 correspond a une case vide
			if tab[line][row] != 0:
				val = tab[line][row]
				for i in range(0, 9):
					#check le carre de 3*3
					if val == tab[i%3+3*(line//3)][i//3+3*(row//3)]\
					and line != i%3+3*(line//3) and row != i//3+3*(row//3):
						print(i%3+3*(line//3), i//3+3*(row//3))
						return False
					#check la ligne
					if val == tab[i][row] and line != i:
						print(i, row)
						return False
					#check la colonne
					if val == tab[line][i] and row != i:
						print(line, i)
						return False
	return True

def ft_can_place(tab, line, row, nb):
	"""check si on peut place le nb dans le tableau"""
	for i in range(0, 9):
		#check le carre de 3*3
		cl = i%3+3*(line//3)
		cr = i//3+3*(row//3)
		if tab[cl][cr] != 0 and line != cl and row != cr\
		and nb == tab[cl][cr]:
			return False
		#check la ligne
		if tab[i][row] != 0 and line != i and nb == tab[i][row]:
			return False
		#check la colonne
		if tab[line][i] != 0 and row != i and nb == tab[line][i]:
			return False
	return True

def solveur(tab, line, row):
	"""fonction recursive qui rempli le tebleau"""
	if line > 8:
		ft_add_glob()
		return ft_append_tab(tab)
	elif row > 8:
		return solveur(tab, line + 1, 0)
	elif tab[line][row] != 0:
		return solveur(tab, line, row + 1)
	elif tab[line][row] == 0:
		for nb in range(1, 10):
			if ft_can_place(tab, line, row, nb) == True:
				tab[line][row] = nb
				solveur(tab, line, row + 1)
				tab[line][row] = 0


def ft_start(content):
	"""fonction principale du fichier permet de lancer les fonction secondaire"""
	tab = ft_get_tab(content)
	ft_write_file("", get_file_to_write_name())
	if ft_first_check(tab) == True:
		solveur(tab, 0, 0)
		print("nb de solution :", nb_sol)
	else :
		ft_write_file("map error", get_file_to_write_name())

if __name__ == '__main__':
	import os
	print("ce programme n'est pas le principale, executer sudoku.py")
	os.system("pause")