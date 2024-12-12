from math import *

def distance(X: list, Y: list, nx: int) :
	"""Renvois la distance entre X et Y, tout deux de tailles nx"""
	dist : int = 0
	
	for i in range (nx) :
		dist += (X[i] - Y[i])**2
	
	dist = sqrt(dist)
	return dist


def barycentre(M: list, n : int, m : int, MX : list, nx : int, u: int, uTot : int) :
	"""Calcule le barycentre de u par rapport au jeu de M (sous la forme de vecteur stocker dans MX)""" 
	
	Xu = [0 for i in range (nx)]	#Vecteur barycentre de u
	
	for i in range (m) :	#Pour chaque jeu
		
		for j in range (nx):	#Pour chaque composante du vecteur
			Xu[-1] += MX[i][j] * M[u][i] / uTot
		
	return Xu


def valeurHypp( dist : float, distmax : float, distmin : float) :
	"""Hyppothèse: distmax > dist > distmin"""
	"""Donne une valeur hyppotétique de j pour X"""
	
	return utot*(dist-distmin)/(distmax-distmin)



def contenus(M :int , n : int, m : int, MX : list, nx : int , u : int, utot : int) :
	"""Renvois un tableau des notes hyppotéthiques pour u pour les jeux non joués de M de taille n x m, les jeux sont représentés par des vecteurs de taille nx dans MX"""
	
	notes = [ 0 for i in range (m) ]
	dist = [ 0. for i in range (m) ]
	
	Xu = barycentre(M, n, m, MX, nx, u, utot)	#barycentre
	
	distmax = 0;
	distmin = 0;
	
	for i in range (m) :	#On calcule les distances au barycentre
		
		dist[i] = distance(MX[i], Xu, nx)
		
		if M[u][i] > 0 and dist[i] > distmax :
			distmax = dist[i]
			
		elif M[u][i] > 0 and dist[i] < distmin :
			distmin = dist[i]
	
	
	for i in range (m) :	#On donne les notes
		
		if M[j][i] == 0 :	#Si le jeu n'a jamais été joué
			notes[i] = valeurHypp(dist[i], distmax, distmin)
	
	return notes


