# -*-coding:utf-8 -*

from donnes import *

def ft_get_tab_content(tab):
	"""permet d'obtenir le contenue d'un tableau
	renvoie sous forme de str"""
	src = " _ _ _ _ _ _ _ _ _"
	for y in range(0, 9):
		src += "\n|"
		for i in range(0, 9):
			src += str(tab[y][i])
			src += "|"
		src += "\n _ _ _ _ _ _ _ _ _"
	print (src)
	return src

def ft_read_file(fname):
	"""fonction quji permet de lire le
	contenue d'un fichier et de le renvoie"""
	content = ""
	with open(fname, "r") as f:
		for line in f:
			content += line
	return content

def ft_write_file(content, fname):
	"""fonction qui permet d'ecrire dans un fichier"""
	with open(fname, "w") as f:
		f.write(content)

def ft_append_file(content, fname):
	"""fonction qui permet d'ajouter un contenue
	au contenue existant d'un fichier"""
	with open(fname, "a") as f:
		f.write(content)

def ft_append_tab(tab):
	"""permet d'appeler les fonctions necessaire pour
	imprimer le tab a 2d du sudoku"""
	ft_append_file("\n", get_file_to_write_name())
	ft_append_file(ft_get_tab_content(tab), get_file_to_write_name())


if __name__ == '__main__':
	import os
	print("ce programme n'est pas le principale, executer sudoku.py")
	os.system("pause")