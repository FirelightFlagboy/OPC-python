# -*-coding:utf-8 -*

import os

def init_tab():
	tab = []
	for l in range(0, 3):
		tab.append([])
		tab[l] = [0 for i in range(0, 3)]
	return tab

def ft_get_val_tab(tab):
	ls = [0,0,0,0,0,0,0,0]
	for x in range(0, 3):
		for y in range(0, 3):
			ls[x] += tab[x][y]
			ls[x+3] += tab[y][x]
		ls[6] += tab[x][x]
		ls[7] += tab[2-x][x]
	return ls

def ft_game_is_over(tab, nb_tour):
	count1 = 0
	count2 = 0
	if nb_tour > 4:
		val = ft_get_val_tab(tab)
		for i, nb in enumerate(val):
			count1 += nb - 1 if nb > 1 else 0
			count2 += (-nb) - 1 if nb < -1 else 0
		print(count1, count2, nb_tour)
		if count1 > 1:
			return 1
		if count2 > 1:
			return 2
		if nb_tour > 7:
			return -1
	return 0

def get_input_pos():
	pos = [-1,-1]
	for i,entier in enumerate(pos):
		error = 1
		while error == 1:
			error = 0
			r = input("entrer la {} sur laquel vous-voulez jouer\n>>>"\
				.format("ligne" if i == 0 else "colonne"))
			try:
				pos[i] = int(r)
				if pos[i] < 1 or pos[i] > 3:
					raise ValueError("le nb de la {} doit etre compris entre 1 et 3"\
						.format("ligne" if i == 0 else "colonne"))
			except Exception as e:
				print(e)
				error = 1
	return pos[0] - 1, pos[1] - 1

def ft_get_pos(tab):
	free = 0
	while free != 1:
		x, y = get_input_pos()
		if tab[x][y] != 0:
			print("les coordonnée {} sont dejas prise.\nVellez les re-saisir"\
				.format((x + 1, y + 1)))
		else:
			free = 1
	return x, y

def ft_place_coor(tab, pos, joueur1):
	x, y = pos
	tab[x][y] = 1 if joueur1 == True else -1

def ft_dysplay_tab(tab):
	src = ""
	for i,line in enumerate(tab):
		src += " - - -\n|"
		for y, nb in enumerate(line):
			if nb == 0:
				src += " |"
			else :
				src += ("X" if nb == 1 else "O") + "|"
		src += "\n"
	src += " - - -\n"
	print(src)

def main():
	tab = init_tab()
	joueur1 = False
	game = 0
	nb_tour = 0
	while game == 0:
		nb_tour += 1
		joueur1 = False if joueur1 == True else True
		print("au tour du joueur {} de jouer".format(1 if joueur1 == True else 2))
		ft_dysplay_tab(tab)
		x, y = ft_get_pos(tab)
		ft_place_coor(tab, (x, y), joueur1)
		game = ft_game_is_over(tab, nb_tour)
	if game < 0:
		print("égalité")
	else:
		print("le jouer {} à gagne".format(game))
	os.system("pause")

if __name__ == '__main__':
	main()