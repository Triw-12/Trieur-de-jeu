from django.test import TestCase
from board_games.recommandation.contenus import *

class ContenuTest(TestCase):
	def setUp(self):
		self.X0 = [1,0,0]
		self.X1 = [0,1,0]
		self.X2 = [2,0,0]
		self.X3 = [1,1,1]

		self.u0 = [4,0,0,0]
		self.u1 = [0,0,0,0]
		self.u2 = [0,4,4,4]
		self.u3 = [0,8,0,8]

		self.nb_jeux_joues = [self.u0, self.u1, self.u2, self.u3]
		self.vecteur_jeux = [self.X0, self.X1, self.X2, self.X3]

	def testDistance(self):
		"""distance(v1: list, v2: list)"""
		self.assertEqual(distance(self.X0, self.X2), 1)
		self.assertEqual(distance(self.X2, self.X0), 1)
		self.assertEqual(distance(self.u0, self.u1), 4)
		self.assertEqual(distance(self.u1, self.u0), 4)
		self.assertEqual(distance(self.u2, self.u2), 0)

	def testDistancePond(self):
		"""distancePond(v1: list, v2: list)"""
		self.assertEqual(distancePond(self.X0, self.X0), 0)
		self.assertEqual(distancePond(self.X0, self.X2), distancePond(self.X2, self.X0))
		self.assertEqual(distancePond(self.X0, self.X1), 4)

	def testBarycentre(self):
		"""barycentre(nb_jeux_joues: list, vecteur_jeux : list, joueur: int, nb_total_jouer : int)"""
		self.assertEqual(barycentre(self.nb_jeux_joues, self.vecteur_jeux, 1, 0), [0, 0, 0])
		self.assertEqual(barycentre(self.nb_jeux_joues, self.vecteur_jeux, 0, 4), [1, 0, 0])

	def testValeurHypp(self):
		"""valeurHypp(dist: float, distmax: float, distmin: float, plus_jouer: int)"""
		self.assertEqual(valeurHypp(20, 30, 10, 30), 15)
		self.assertEqual(valeurHypp(1, 1, 1, 1), 1)

	def testContenus(self):
		"""contenus(nb_jeux_joues: list, vecteur_jeux: list, joueur: int, nb_jeux_jouee_par_joueur: int)"""
		self.assertEqual(contenus(self.nb_jeux_joues, self.vecteur_jeux, 1, 0), [0, 0, 0, 0])
		self.assertEqual(int(contenus(self.nb_jeux_joues, self.vecteur_jeux, 3, 16)[0]), 4)
