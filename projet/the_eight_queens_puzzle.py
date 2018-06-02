# -*-coding:utf-8 -*

import os
from array import array

nb_sol = 0

def ft_add_glob():
	global nb_sol
	nb_sol += 1

def ft_print_sol_fast(tab):
	src = str()
	for i in range(0,8):
		src += str(tab[i] + 1) + " "
	print(src)

def ft_print_sol_fancy(tab):
	src = "._._._._._._._._.\n"
	for line in range(0, 8):
		src += "|"
		for row in range(0, 8):
			if row == tab[line]:
				src += "X"
			else:
				src += " "
			src += "|"
		src += "\n._._._._._._._._.\n"
	print(src)

def ft_is_free(tab, line, row):
	boolean = True
	for li in range(0, line):
		ro = 0
		for ro in range(0, 8):
			r = tab[li]
			boolean = boolean and (True if (abs(line - li) != abs(row - r)) and row != r else False)
	return boolean

def ft_place_queens(tab, line, dysplay):
	row = 0
	if line >= 8:
		if dysplay == 1:
			ft_print_sol_fancy(tab)
		elif dysplay == 2:
			ft_print_sol_fast(tab)
		ft_add_glob()
	else:
		for row in range(0, 8):
			if ft_is_free(tab, line, row):
				tab[line] = row
				ft_place_queens(tab, line + 1, dysplay)
				tab[line] = 0
	pass

def ft_cmp(s1, s2):
	l1 = len(s1)
	l2 = len(s2)
	i = 0
	while i < l1 and i < l2 and s1[i] == s2[i]:
		i += 1
	if i >= l1 and i >= l2:
		return 0
	elif i >= l1 and i < l2:
		return -ord(s2[i])
	elif i < l1 and i >= l2:
		return ord(s1[i])

def main():
	"""lancer la fonction qui vas chercher
	les solutions"""
	print("====Dysplay Method====")
	print("-1 fancy/slow")
	print("-2 fast/speed")
	print("======================")
	error = 1
	while error == 1:
		error = 0
		choice = input("saisissez option :\n>>>")
		try:
			choice = int(choice)
		except (TypeError, ValueError, NameError) as e:
			print("impossible de convertir \"{}\" en integer".format(choice))
			error = 1

	dysplay = choice
	tab = array('i')
	for i in range(0,8):
		tab.append(0)
	ft_place_queens(tab,0, dysplay)
	print("nb de solution :", nb_sol)
	os.system("pause")

if __name__ == '__main__':
	"""permet de lancer le programme principale"""
	main()