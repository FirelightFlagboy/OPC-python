import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../Class'))
from Class.Carte import Carte

class CarteTest(unittest.TestCase):

	"""
	Test la class Carte de Carte.py
	"""
	def setUp(self):
		"""setup le test set"""
		self.test = {
			"zeroNl" : "OOOOOO",
			"sixNl" : "\n\n\n\n\n",
			"fullmap" :
				"OOOOOOOO\n"
				"O     UO\n"
				"OOOOOOOO",
			"fullmapDoor" :
				"OOOOOOOO\n"
				"O .   UO\n"
				"OOOOOOOO"
		}

		self.maze = {}
		for key, val in self.test.items():
			self.maze[key] = Carte(key, val)

	def testConvStrDic(self):
		"""
		Verifier si la conversion de la chaine vers un dic et bien faite
		"""
		zeroNl = {
			(1, 1) : "O",
			(1, 2) : "O",
			(1, 3) : "O",
			(1, 4) : "O",
			(1, 5) : "O",
			(1, 6) : "O"
		}
		sixNl = {
			(1, 1) : "\n",
			(2, 1) : "\n",
			(3, 1) : "\n",
			(4, 1) : "\n",
			(5, 1) : "\n"
		}
		fullmap = {
			(1, 1) : "O", (2, 1) : "O", (3, 1) : "O",
			(1, 2) : "O", (2, 2) : " ", (3, 2) : "O",
			(1, 3) : "O", (2, 3) : " ", (3, 3) : "O",
			(1, 4) : "O", (2, 4) : " ", (3, 4) : "O",
			(1, 5) : "O", (2, 5) : " ", (3, 5) : "O",
			(1, 6) : "O", (2, 6) : " ", (3, 6) : "O",
			(1, 7) : "O", (2, 7) : "U", (3, 7) : "O",
			(1, 8) : "O", (2, 8) : "O", (3, 8) : "O",
			(1, 9) : "\n", (2, 9) : "\n"
		}
		self.assertEqual(self.maze["zeroNl"].labyrinthe, zeroNl)
		self.assertEqual(self.maze["sixNl"].labyrinthe, sixNl)
		self.assertEqual(self.maze["fullmap"].labyrinthe, fullmap)

	def testPickRandomLocation(self):
		"""
		Test la methode pour obtenir une coordonnée libre
		"""
		coordZero = self.maze["zeroNl"].pickRandomLocation()
		coordfive = self.maze["sixNl"].pickRandomLocation()
		coordfull = self.maze["fullmap"].pickRandomLocation()

		# vu que les 2 premier map n'ont pas deplacement libre
		# les coordonnée renvoie doivent etre null
		self.assertIsNone(coordZero)
		self.assertIsNone(coordfive)
		# on verifie si les coordonnée sont bien register dans le dictionnaire
		self.assertIn(coordfull, self.maze["fullmap"].labyrinthe)
		# puis si la val qui se trouve a la key est bien un espace vide
		self.assertEqual(self.maze["fullmap"].labyrinthe[coordfull], " ")

	def test__str__(self):
		"""
		Test la methode __str__
		"""
		for key, val in self.test.items():
			so = "test : " + val
			sv = "test : " + self.maze[key].__str__()
			self.assertEqual(sv, so)

	def test__repr__(self):
		"""
		Test la methode __repr__
		"""
		for key, val in self.maze.items():
			so = "<Carte " + key + ">"
			self.assertEqual(so, val.__repr__())

	def testRobotCanMove(self):
		"""
		verifie la methode robotCanMove
		"""
		fullmap = self.maze["fullmap"]
		coord1 = (2, 1)
		coord2 = (2, 2)
		coord3 = (1, 4)
		# test toute les directions
		# les coord1 et 3 sont toujours fausse
		for l in "nsew":
			self.assertFalse(fullmap.actionOk(coord1, l, l, 1))
			self.assertFalse(fullmap.actionOk(coord3, l, l, 1))

		# pour la coord2 le robot peut seulement se deplacer a l'est
		# sur 6 case en content celle de depart
		self.assertFalse(fullmap.actionOk(coord2, "n", "n", 1))
		self.assertFalse(fullmap.actionOk(coord2, "s", "s", 1))
		self.assertFalse(fullmap.actionOk(coord2, "o", "o", 1))

		self.assertTrue(fullmap.actionOk(coord2, "e", "e", 1))
		self.assertTrue(fullmap.actionOk(coord2, "e", "e", 5))

	def testRobotCanWork(self):
		"""
		verifie la methode robotCanWork
		"""
		fullmapDoor = self.maze["fullmapDoor"]
		coord = (2, 2)
		# test la methode murer
		# le nord, sud, ouest correspond a des murs sur la map
		self.assertFalse(fullmapDoor.actionOk(coord, "m", "n"))
		self.assertFalse(fullmapDoor.actionOk(coord, "m", "s"))
		self.assertFalse(fullmapDoor.actionOk(coord, "m", "o"))
		# la porte se trouve a l'est du robot
		self.assertTrue(fullmapDoor.actionOk(coord, "m", "e"))

		# le nord, sud, ouest correspond a des murs sur la map
		self.assertTrue(fullmapDoor.actionOk(coord, "p", "n"))
		self.assertTrue(fullmapDoor.actionOk(coord, "p", "s"))
		self.assertTrue(fullmapDoor.actionOk(coord, "p", "o"))
		# la porte se trouve a l'est du robot
		self.assertFalse(fullmapDoor.actionOk(coord, "p", "e"))

	def testBuildWall(self):
		"""
		verifie la methode testBuildWall
		"""
		fullmapDoor = self.maze["fullmapDoor"]
		# on choisi une coordone contenent un mur
		coord = (2, 3)
		res = "OOOOOOOO\nO O   UO\nOOOOOOOO"

		# la fonction renvoie true si elle a placer un mur
		self.assertTrue(fullmapDoor.buildWall(coord))
		# si le mur est bien placer alors la map a du changer
		self.assertEqual(fullmapDoor.__str__(), res)

		# sinon elle renvoie false si il ne s'agit pas d'une porte
		self.assertFalse(fullmapDoor.buildWall(coord))
		self.assertEqual(fullmapDoor.__str__(), res)

	def testBuildDoor(self):
		"""
		verifie la methode testBuildDoor
		"""
		fullmapDoor = self.maze["fullmapDoor"]
		res = "O.OOOOOO\n. .   UO\nO.OOOOOO"
		lst = [(1, 2), (2, 1), (3, 2)]

		# la fonction renvoie true si elle a placer une porte
		for l in lst:
			self.assertTrue(fullmapDoor.buildDoor(l))

		# sinon elle renvoie false si il ne s'agit pas d'un mur
		self.assertFalse(fullmapDoor.buildDoor((2, 2)))
		self.assertFalse(fullmapDoor.buildDoor((2, 3)))
		self.assertEqual(fullmapDoor.__str__(), res)

