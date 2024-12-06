from math import *


def moyenne(M : list, m : int,  u : int):
	#Hyppothèse: m est la taille de M, m>0
	#Renvois la moyenne de u des parties par rapport au jeu dans M
	
	moy : float= 0
	for i in range(m) :
		moy += M[u][i]
	
	return (moy/m)
	


def Pearson(M: list, u: int, v: int, u_moy : float, v_moy : float):
	# Renvois la Correlation de Pearlson entre u et v selon M
	
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
	#Renvois une note hyppothétique de j pour u
	
	n : int = len(M)
	m : int = len(M[0])
	u_moy : float = moyenne(M, m, u)
	
	Pear = 0
	Pearpond = 0
	
	for v in range(n) :
		if M[v][j] > 0 :
			v_moy = moyenne(M, m, v)
			P = Pearson(M, u, v, u_moy, v_moy)
			Ppuiss = pow(abs(P),1.5) * P
			Pear += Ppuiss
			Pearpond = (M[v][j] - v_moy) * Ppuiss
	
	return (u_moy + (Pearpond/Pear))

def filtrageCollaboratif(M,u) :
	L : list = []
	
	for j in range(len(M[u])):
		if (M[u][j] == 0) :
			L.append(MoyPon(M,u,j))
		else :
			L.append(0)
	
	return L



M = [[4,4,3,0,2],[2,1,4,0,0],[2,1,4,2,4]]

print(filtrageCollaboratif(M,1))
