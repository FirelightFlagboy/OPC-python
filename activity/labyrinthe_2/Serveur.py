from Class.Carte import Carte
from Class.Maps import Maps
from Class.Robot import Robot
from Class.Serveur import Serveur
import socket
import select
import os
import sys
import signal

# le repertoire ou se trouve les maps
dirToMap = "map"
# nom de l'hote
hote = ""
# port du serveur
port = 12800
# class serveur
server = None

def sigint_handler(n, stack):
	global server
	if server:
		del server
	sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

"""
on choisi la map
"""
maps = Maps(dirToMap)
maps.readFromListDir()
carte = maps.getMapFromChoice()
del maps

# creer une instance de la class serveur
server = Serveur(carte, hote, port)
# on supprime la liste de carte
del carte
# maintenant on attendent les jouers le reste des fonctions serat appele automatiquement
server.getClient()
