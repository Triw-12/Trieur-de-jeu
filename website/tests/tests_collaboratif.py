from django.test import TestCase

from board_games.recommandation.collaboratif import *

class CollaboratifTest(TestCase):
	def setUp(self):
		self.X0 = [1,0,0]
		self.X1 = [0,1,0]
		self.X2 = [2,0,0]
		self.X3 = [1,1,1]

		self.u0 = [4,0,0,0]
		self.u1 = [0,0,0,0]
		self.u2 = [0,4,4,4]
		self.u3 = [0,8,0,8]

		self.mu0 = 1
		self.mu1 = 0
		self.mu2 = 3
		self.mu3 = 4

		self.nb_jeux_joues = [self.u0, self.u1, self.u2, self.u3]
		self.vecteur_jeux = [self.X0, self.X1, self.X2, self.X3]

	def testPearson(self):
		"""pearson(nb_jeux_joues: list, joueur1: int, joueur2: int, joueur1_moyenne : float, joueur2_moyenne : float)"""
		self.assertEqual(pearson(self.nb_jeux_joues, 0, 1, self.mu0, self.mu1), 0)
		self.assertEqual(pearson(self.nb_jeux_joues, 0, 0, self.mu0, self.mu0), 1)
		self.assertEqual(pearson(self.nb_jeux_joues, 0, 2, self.mu0, self.mu2), -1)

	def testMoyennePonderee(self):
		"""moyennePonderee(nb_jeux_joues: list, joueur: int, jeu: int)"""
		self.assertEqual(int(moyennePonderee(self.nb_jeux_joues, 0, 1)), 0)
		self.assertEqual(int(moyennePonderee(self.nb_jeux_joues, 2, 3)), 4)
		self.assertEqual(moyennePonderee(self.nb_jeux_joues, 1, 0), 0)

	def testCollaboratif(self):
		"""collaboratif(nb_jeux_joues : list, joueur : int)"""
		self.assertEqual(collaboratif(self.nb_jeux_joues, 0)[2], 0)
		self.assertEqual(collaboratif(self.nb_jeux_joues, 1), [0, 0, 0, 0])
		self.assertEqual(int(10 * collaboratif(self.nb_jeux_joues, 2)[1]), 46)
