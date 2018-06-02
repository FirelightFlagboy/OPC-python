# -*-coding:utf-8 -*

#test si une année est bissextile
a = input("saisissez une annee a : ")

a = int(a)

test = False

if a%4 ==0:
	test = True
	if a%100 == 0 and a%400 != 0:
		test = False
		
else:
	test = False

if test == True:
	print("l'annee ",a," est bissextile")
else:
	print("l\'annee ",a," n\'est pas bissextile")