from math import *



	

def Pearson(M: list, u: int, v: int, u_moy : float, v_moy : float):
	""" Renvois la Correlation de Pearlson entre u et v selon M"""
	
	m : int = len(M[0])
	scalair : float = 0
	ecard_u : float = 0
	ecard_v : float = 0
	
	for i in range(m):
		if M[u][i]*M[v][i] != 0 :
			scalair += (M[u][i] - u_moy) * (M[v][i] - v_moy)
			ecard_u +=  (M[u][i] - u_moy) * (M[u][i] - u_moy)
			ecard_v += (M[v][i] - v_moy) * (M[v][i] - v_moy)
	
	return (scalair/ (sqrt(ecard_u * ecard_v)))


def MoyPon(M: list, u: int, j: int):
	"""Renvois une note hyppothétique de j pour u"""
	
	n : int = len(M)
	m : int = len(M[0])
	u_moy : float = sum(M[u])/m
	
	Pear = 0
	Pearpond = 0
	
	for v in range(n) :
		if M[v][j] > 0 :
			v_moy = sum(M[v])/m
			P = Pearson(M, u, v, u_moy, v_moy)
			Ppuiss = pow(abs(P),1.5) * P
			Pear += Ppuiss
			Pearpond = (M[v][j] - v_moy) * Ppuiss
	
	return (u_moy + (Pearpond/Pear))


def collaboratif(M : list, m : int, n : int, u : int) :
	"""Hyppothèse: M est de taille m*n ; u<m"""
	"""Renvois des notes hyppothétiques pour le joueur u à partir de M"""
	notes : list = [0 for i in range(n)]
	
	for j in range(n):
		
		if (M[u][j] == 0) :	#Pour les jeux jamais joués
			notes[j] = MoyPon(M,u,j)

	
	return notes



M = [[2,1,4,0,0],[2,1,4,2,4]]

print(collaboratif(M,2,5,0))
