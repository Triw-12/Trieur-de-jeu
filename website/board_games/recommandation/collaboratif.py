from math import *

def pearson(nb_jeux_joues: list, joueur1: int, joueur2: int, joueur1_moyenne : float, joueur2_moyenne : float):
	""" Renvoie la Correlation de Pearson entre joueur1 et joueur2 selon nb_jeux_joues"""
	
	m : int = len(nb_jeux_joues[0])
	scalaire : float = 0
	ecard_u : float = 0
	ecard_v : float = 0
	
	for i in range(m):
		if nb_jeux_joues[joueur1][i]*nb_jeux_joues[joueur2][i] != 0 :
			scalaire += (nb_jeux_joues[joueur1][i] - joueur1_moyenne) * (nb_jeux_joues[joueur2][i] - joueur2_moyenne)
			ecard_u +=  (nb_jeux_joues[joueur1][i] - joueur1_moyenne) * (nb_jeux_joues[joueur1][i] - joueur1_moyenne)
			ecard_v += (nb_jeux_joues[joueur2][i] - joueur2_moyenne) * (nb_jeux_joues[joueur2][i] - joueur2_moyenne)
	
	return (scalaire/ (sqrt(ecard_u * ecard_v)))


def moyennePonderee(nb_jeux_joues: list, joueur: int, j: int):
	"""Renvoie une note hyppothétique de j pour joueur"""
	
	n : int = len(nb_jeux_joues)
	m : int = len(nb_jeux_joues[0])
	joueur_moyenne : float = sum(nb_jeux_joues[joueur])/m
	
	pear = 0
	pearpond = 0
	
	for joueur2 in range(n) :
		if nb_jeux_joues[joueur2][j] > 0 :
			joueur2_moyenne = sum(nb_jeux_joues[joueur2])/m
			res_pearson = pearson(nb_jeux_joues, joueur, joueur2, joueur_moyenne, joueur2_moyenne)
			ppuiss = pow(abs(res_pearson),1.5) * res_pearson
			pear += ppuiss
			pearpond = (nb_jeux_joues[joueur2][j] - joueur2_moyenne) * ppuiss
	
	return (joueur_moyenne + (pearpond/pear))


def collaboratif(nb_jeux_joues : list, joueur : int) :
	"""Hypothèse: nb_jeux_joues est de taille m*n ; joueur<m"""
	"""Renvois des notes hyppothétiques pour le joueur joueur à partir de nb_jeux_joues"""
	n = len(nb_jeux_joues[0])
	notes : list = [0 for _ in range(n)]
	
	for j in range(n):
		
		notes[j] = moyennePonderee(nb_jeux_joues,joueur,j)

	
	return notes
