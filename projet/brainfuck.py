#coding:utf-8

"""
- chercher comment convertir un certian index de la table ascii vers son char correspondant:
	voir utilisé une liste de char contenent tout les caractères de la table ascii index 10 correspondrait au char de val 10
	dans la table ascii
- voir comment creer un string vide:
	voir utilisé un dictionnaire avec pour clée un int allant de 0 à len desirer
"""

from os import system
import random

def ft_get_dic(size):
	dic = {}
	for i in range(0, size):
		dic[i] = 0
	return dic

def brianfuck(michel):
	dic = ft_get_dic(50)
	print(dic)
	return "bonjour"

def ft_print_dic(dic):
	ls = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','v']
	for key in dic.keys():
		print(ls[dic[key]], end="")

def main():
	jacque = input("enter brian to decode as fuck :\n")
	result = brianfuck(jacque)
	print(result)

if __name__ == '__main__':
	main()
	system("pause")