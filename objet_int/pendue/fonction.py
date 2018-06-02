# -*-coding:utf-8 -*

from random import randrange

def set_name(fname):
	mon_fichier = open(fname)
	lines = [line.rstrip('\n') for line in mon_fichier]
	mon_fichier.close()
	#print(lines)
	nb_line = get_line(fname)
	#print("nb_line >>",nb_line)
	rand = randrange(nb_line)
	return lines[rand].lower()

def set_cname(nameO):
	nameC = ""
	for i in range(0,len(nameO)):
		nameC = nameC + "_"
	return nameC

def get_line(fname):
	with open(fname) as f:
		for i,l in enumerate(f):
			pass
		return i+1

def get_letter():
	l = ''
	while len(l) != 1:
		l = input("saisissez un character >")
	l.lower()
	return l

def isLetterInName(letter,name,nameC):
	bol = 0
	for i in range(0,len(name)):
	#	print(">t> i>{0} name>{1}".format(i,name[i]))
		if(letter == name[i]):
			bol = 1
			nameC = nameC[:i]+letter+nameC[i+1:]

	#print(">t>",nameC)
	return bol,nameC

def test_fin(name,nameC):
	if (name == nameC):
		return 1
	else:
		return 0

def print_score(fname,name,score):
	dic = {}
	name = name.capitalize()
	with open(fname) as f:
		for i,l in enumerate(f):
			cle,sc = l.split(":")
			try:
				sc = int(sc)
			except TypeError as e:
				print("impossible de convertire le score")
			else:
				dic[cle] = "TypeError"
			finally:
				dic[cle] = sc
	print(dic)
	if name in dic.keys():
		dic[name] += score
	else:
		dic[name] = score

	with open(fname,"w") as f:
		for cle,values in dic.items():
			f.write("{0}:{1}\n".format(cle,values))
	sorted_x = sorted(dic.items(), key=lambda x: x[1], reverse = True)

	print("position :    nom:   score:")
	for i, eld in enumerate(sorted_x):
		name,score = eld
		print("{0}. {1} {2}".format(i+1,name,score))


if __name__ == '__main__':
 	import os

 	print("ne contient pas le programme principale,\n>>pendue.py\nce fichier contient les fonctions du programme principale.")

 	os.system("pause")