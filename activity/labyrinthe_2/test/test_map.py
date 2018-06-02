import io
import re
import os
import sys
import unittest
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../Class'))
from Maps import Maps

class MapsTest(unittest.TestCase):

	"""
	Class de test pour la class Maps
	"""

	def setUp(self):
		"""
		Setup necessaire pour le test
		"""
		# load class maps
		self.map = Maps("test")
		# get regex expression for user choice of map
		self.ex_choice_map = self.map.ex_choice
		# get regex expression for content of map file
		self.ex_content_map = self.map.ex_content

	def testChoiceGoodInputMap(self):
		"""
		Test si l'utilisateur a bien saissie un nombre
			(celui ci correspond a l'index de la map choisi)
		"""

		choiceSimple = "1"
		choiceBig = "124654987532156489"

		self.assertNotEqual(re.search(self.ex_choice_map, choiceSimple), None)
		self.assertNotEqual(re.search(self.ex_choice_map, choiceBig), None)

	def testChoiceBadInputMap(self):
		"""
		verifie si la regex marche correctement lorsque l'utilisateur saisie
		un mauvais input
		"""
		choiceNegSimple = "-1"
		choiceNegBig = "-123548796"

		self.assertEqual(re.search(self.ex_choice_map, choiceNegSimple), None)
		self.assertEqual(re.search(self.ex_choice_map, choiceNegBig), None)

		choiceYolo = "Yolo"
		choiceNumberYolo = "123yolo456"

		self.assertEqual(re.search(self.ex_choice_map, choiceYolo), None)
		self.assertEqual(re.search(self.ex_choice_map, choiceNumberYolo), None)

		choiceDot1 = "123."
		choiceDot2 = ".123"
		choiceDot3 = "1.23"

		self.assertEqual(re.search(self.ex_choice_map, choiceDot1), None)
		self.assertEqual(re.search(self.ex_choice_map, choiceDot2), None)
		self.assertEqual(re.search(self.ex_choice_map, choiceDot3), None)

	def testContentGoodMap(self):
		"""
		Test si le contenue d'une map est conpatible c-a-d pas de charactere
		autre que 'U', ' ', '\n', 'O'
		"""
		mapSimple = "OOOOOOOOOO\nO        U\nOOOOOOOOOO"
		mapNoExit = "OOOOOOOOOO\nO        O\nOOOOOOOOOO"
		mapExtraChar = "OOOOOOOOOO\nOX       U\nOOOOOOOOOO"
		mapNoSpace = "OOOOOOOOOO\nOU\nOOOOOOOOOO"

		self.assertTrue(self.map.isMapContentOk(mapSimple))

		self.assertFalse(self.map.isMapContentOk(mapNoExit))
		self.assertFalse(self.map.isMapContentOk(mapExtraChar))
		self.assertFalse(self.map.isMapContentOk(mapNoSpace))

	def testBadDir(self):
		"""
		Test si la fonction scan renvoie bien une liste vide en cas d'erreur
		"""
		# test avec un repetoire qui n'existe pas
		# et que le message d'erreur est correct
		new_out_BadDir, new_err_BadDir = io.StringIO(), io.StringIO()
		sys.stdout, sys.stderr = new_out_BadDir, new_err_BadDir
		resBadDir = self.map.searchFormDir("folderthatdoesn'texist")

		# test avec un fichier qui n'est pas un dossier
		# et que le message d'erreur est correct
		new_out_IsFile, new_err_IsFile = io.StringIO(), io.StringIO()
		sys.stdout, sys.stderr = new_out_IsFile, new_err_IsFile
		resIsFile = self.map.searchFormDir(__file__)

		# reset les sortie standard
		sys.stdout, sys.stderr = sys.__stdout__, sys.__stderr__

		# en cas d'erreur une liste vide et retourner
		self.assertEqual(resBadDir, [])
		self.assertEqual(resIsFile, [])

		# test les messages d'erreur
		# recupere les strings contenue dans les io string
		outBad, errBad = new_out_BadDir.getvalue(), new_err_BadDir.getvalue()
		outFile, errFile = new_out_IsFile.getvalue(), new_err_IsFile.getvalue()

		# le message doit s'afficher sur la sortie d'erreur
		self.assertEqual(outBad, "")
		self.assertEqual(outFile, "")

		self.assertEqual(errBad, "folderthatdoesn'texist doesn't exist\n")
		self.assertEqual(errFile, __file__ + " not a directory\n")
		# fermer les io string
		new_out_BadDir.close()
		new_err_BadDir.close()
		new_out_IsFile.close()
		new_err_IsFile.close()

	def testNoMap(self):
		"""
		verifie si le programme quite avec le bon message d'erreur
		si aucune map n'a etait trouver et que on demande a l'utilisateur de choisir
		"""

		# creer 2 io string
		new_out, new_err = io.StringIO(), io.StringIO()
		sys.stdout, sys.stderr = new_out, new_err

		# verifie si le programme exit bien si aucune map n'a etait trouver
		with self.assertRaises(SystemExit):
			self.map.getMapFromChoice()

		# reset les sorties standard
		sys.stdout, sys.stderr = sys.__stdout__, sys.__stderr__

		out, err = new_out.getvalue(), new_err.getvalue()

		self.assertEqual(out, "")
		self.assertEqual(err, "no map found\n")

		# ferme les io string
		new_out.close()
		new_err.close()
