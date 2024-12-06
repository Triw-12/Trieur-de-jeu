from math import *


def Cosine(X: list, Y: list, n: int) :
	"""Renvois la similarité de x et y, tout de de taille n"""
	num : float = 0
	denX : float = 0
	denY : float = 0
	
	for i in range (n):
		num += X[i] * Y[i]
		denX += X[i] * X[i]
		denY += Y[i] * Y[i]
	
	cosine : float = num/(sqrt(denX)*sqrt(denY))
		
def MatriceCosine (G : list, m : int) :
	"""Renvois une matrice m*m des cosines des jeux de G"""
	Cos = []

	for g1 in G :
		Cos.append([])

		for g2 in G :

			if g2 = g1 :
				Cos[-1].append(0)

			else :
				Cos[-1].append(Cosine(g1,g2))


def filtrageParContenue (M : list, G : list , n : int, m : int, u : int):
	"""Hyppothèse: M est de taille n*m"""
	"""Renvois une liste de jeu recommandé pour u, du plus recommandé au moins recommandé"""

	MatCos = MatriceCosine(G,m)

	gmax = max(M[u]);
	return max(MatCos[gmax])
		