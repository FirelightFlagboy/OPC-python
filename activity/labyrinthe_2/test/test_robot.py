import unittest
import io
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../Class'))
from Robot import Robot
from Carte import Carte

class testRobot(unittest.TestCase):

	"""
	test la classe Robot
	"""

	def setUp(self):
		self.map = Carte("fullmap", "OOOOOOOO\nO .   UO\nOOOOOOOO")
		self.robot1 = Robot(1, 1, "robot1")
		self.robot2 = Robot(2, 2, "robot2")
		self.robot3 = Robot(2, 5, "robot3")
		self.robot4 = Robot(2, 1, "robot4")

	def testNeedMouvement(self):
		"""
		verifie la methode testNeedMouvement
		"""

		robot1 = Robot(1, 1, "robot1")
		robot2 = Robot(2, 2, "robot2")
		robot3 = Robot(2, 5, "robot3")
		robot4 = Robot(2, 1, "robot4")
		# renvoie vrai si aucun mouvement est set
		self.assertTrue(robot1.needMovement(self.map))
		self.assertTrue(robot2.needMovement(self.map))
		self.assertTrue(robot3.needMovement(self.map))
		self.assertTrue(robot4.needMovement(self.map))

		robot1.setMovement("n", "n", 1)
		robot2.setMovement("e", "e", 1)
		robot3.setMovement("e", "e", 1)
		robot4.setMovement("m", "s", 1)

		# renvoie vrai si le mouvement est impossible
		self.assertTrue(robot1.needMovement(self.map))
		self.assertTrue(robot4.needMovement(self.map))
		# sinon false
		self.assertFalse(robot2.needMovement(self.map))
		self.assertFalse(robot3.needMovement(self.map))
		pass

	def testUpdate(self):
		"""
		verifie la methode testUpdate
		"""

		robot1 = Robot(1, 1, "robot1")
		robot2 = Robot(2, 2, "robot2")
		robot3 = Robot(2, 5, "robot3")
		robot4 = Robot(2, 1, "robot4")

		robot1.setMovement("n", "n", 1)
		robot2.setMovement("e", "e", 1)
		robot3.setMovement("e", "e", 1)
		robot4.setMovement("m", "s", 1)

		self.assertFalse(robot1.update(self.map))
		self.assertFalse(robot4.update(self.map))

		self.assertTrue(robot2.update(self.map))
		self.assertTrue(robot3.update(self.map))

		self.assertEqual(robot2.coord, (2, 3))
		self.assertEqual(robot3.coord, (2, 6))
		pass

	def test__str__(self):
		"""
		verifie la methode __str__
		"""
		robot1 = Robot(1, 1, "robot1")

		sa = "test : <Robot robot1 (1, 1)>"
		so = "test : " + robot1.__str__()
		self.assertEqual(sa, so)
		pass
