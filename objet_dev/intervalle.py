# -*-coding:utf-8 -*

def intervalle(bMin, bMax):
	"""un generateur qui renvoie les valeur compris
	entre ]bMin;bMax[ """
	for i in range(bMin+1,bMax):
		yield i

if __name__ == '__main__':
	import os
	for i in intervalle(5,10):
		print(i)

	os.system("pause")