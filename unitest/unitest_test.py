import random
import unittest

class randomTest(unittest.TestCase):
	"""
		Test case used for test the function of module 'random'.
	"""

	def setUp(self):
		""" init of test """
		self.liste = list(range(10))

	def test_choice(self):
		""" Test the operation of the function 'random.choice'."""
		elt = random.choice(self.liste)
		# check if elt is in 'self.liste'
		self.assertIn(elt, self.liste)

	def test_shuffle(self):
		""" Test the operation of the function 'random.shuffle'."""
		random.shuffle(self.liste)
		self.liste.sort()
		self.assertEqual(self.liste, list(range(10)))

	def test_sample(self):
		""" Test the operation of the function 'random.sample'."""
		samp = random.sample(self.liste, 5)
		# test simple sampling
		for el in samp:
			self.assertIn(el, self.liste)

		# test error
		self.assertRaises(ValueError, random.sample, self.liste, 20)
		# same test above but with 'with'
		with self.assertRaises(ValueError):
			random.sample(self.liste, 20)
unittest.main()
