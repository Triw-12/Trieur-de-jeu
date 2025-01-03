from math import *



	

def pearson(nb_jeux_joues: list, u: int, v: int, u_moy : float, v_moy : float):
	""" Renvoie la Correlation de Pearson entre u et v selon nb_jeux_joues"""
	
	m : int = len(nb_jeux_joues[0])
	scalaire : float = 0
	ecard_u : float = 0
	ecard_v : float = 0
	
	for i in range(m):
		if nb_jeux_joues[u][i]*nb_jeux_joues[v][i] != 0 :
			scalaire += (nb_jeux_joues[u][i] - u_moy) * (nb_jeux_joues[v][i] - v_moy)
			ecard_u +=  (nb_jeux_joues[u][i] - u_moy) * (nb_jeux_joues[u][i] - u_moy)
			ecard_v += (nb_jeux_joues[v][i] - v_moy) * (nb_jeux_joues[v][i] - v_moy)
	
	return (scalaire/ (sqrt(ecard_u * ecard_v)))


def moyennePonderee(nb_jeux_joues: list, u: int, j: int):
	"""Renvoie une note hyppothétique de j pour u"""
	
	n : int = len(nb_jeux_joues)
	m : int = len(nb_jeux_joues[0])
	u_moy : float = sum(nb_jeux_joues[u])/m
	
	pear = 0
	pearpond = 0
	
	for v in range(n) :
		if nb_jeux_joues[v][j] > 0 :
			v_moy = sum(nb_jeux_joues[v])/m
			res_pearson = pearson(nb_jeux_joues, u, v, u_moy, v_moy)
			ppuiss = pow(abs(res_pearson),1.5) * res_pearson
			pear += ppuiss
			pearpond = (nb_jeux_joues[v][j] - v_moy) * ppuiss
	
	return (u_moy + (pearpond/pear))


def collaboratif(nb_jeux_joues : list, u : int) :
	"""Hypothèse: nb_jeux_joues est de taille m*n ; u<m"""
	"""Renvois des notes hyppothétiques pour le joueur u à partir de nb_jeux_joues"""
	n = len(nb_jeux_joues[0])
	notes : list = [0 for _ in range(n)]
	
	for j in range(n):
		
		notes[j] = moyennePonderee(nb_jeux_joues,u,j)

	
	return notes
