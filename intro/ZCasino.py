# -*-coding:utf-8 -*

import os
from math import ceil
from random import randrange

def recup_nb(min,max,ttype):
    print(ttype)
    test = True
    while test:
        print("selectionner un nb compris entre ",min," et ",max)
        nb = input(">>")
        print(nb)
        try:
                nb = int(nb)
                assert nb >= min and nb <= max
        except TypeError as e:
                print("ERROR > conversion : ",e)
        except AssertionError:
                print("le nb saisi doit être compris entre ",min," et ",max,)
        else:
                test = False

    return nb

                
if __name__ == "__main__":
    credit = 50
    mise = 100
    while credit>=0:
        print("credit actuel : ",credit)
        rand = randrange(50)
        print("rand >>",rand)
        nb = recup_nb(0,49,"choix du nb de la case")
        while 1:
            mise = recup_nb(1,credit,"choix de la mise")
            if mise <= credit:
                break

        print("la bille c'est arreter sur la case ",rand)
        if nb == rand:
            print("bravo tu as misé sur le bon chiffre !\nTa mise est alors tripler")
            credit = credit + ceil(3*mise)
        elif (nb%2 == 0 and rand%2 == 0) or (nb%2 != 0 and rand%2 != 0):
            print("bravo tu as misé sur la même couleur que celle de la bille\ntu reçois +50\% de ta mise en plus de celle ci ")
            credit = credit + ceil(mise/2) + mise
        else:
            print("dommage tu n'as pas eu de chance\ntu perds ta mise")
            credit = credit - mise

    os.system("pause")
