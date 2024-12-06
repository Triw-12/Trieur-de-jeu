from math import *

def distance(X: list, Y: list, n: int) :
	"""Renvois la distance entre X et Y, tout deux de tailles n"""
	dist : int = 0
	
	for i in range (n) :
		dist += (X[i] - Y[i])**2
	
	dist = sqrt(dist)
	return dist

def barycentre(M: list, MX : list, n : int, m : int, u: int, uTot : int) :
	"""Calcule le barycentre de u par rapport au jeu de M (sous la forme de vecteur stocker dans MX)""" 
	
	Xu = []
	
	for i in range (n) :
		Xu.append(0)
		for i in range (m):
			Xu[-1] += MX[i] * M[u][i] / uTot
		
	return Xu


def valeurHypp(MX: list, X : list, n : int, m : int, j : int, utot : int, distmax : float, distmin : float) :
	"""Hyppotèse: MX de taille n*m, X de taille m"""
	"""Donne une valeur hyppotétique de j pour X"""
	
	dist : float = distance(X, XM[j], m)
	
	return utot*(dist-distmin)/(distmax-distmin)
