from math import *

def distance(v1: list, v2: list) :
	"""Renvoie la distance entre v1 et v2, tous deux de même tailles"""
	assert len(v1) == len(v2)
	dist : int = 0
	
	for i in range (len(v1)) :
		
		if i < 2 :	#Pondération par rapport à l'importance du composant
			dist += (8 * (v1[i] - v2[i])) **2
		
		elif i < 6 :
			dist += (5 * (v1[i] - v2[i])) **2
		
		else :
			dist + = (v1[i] - v2[i]) **2
	
	dist = sqrt(dist)
	return dist


def barycentre(nb_jeux_joues: list, vecteur_jeux : list, joueur: int, uTot : int) :
	"""Calcule le barycentre de joueur par rapport au jeu de nb_jeux_joues (sous la forme de vecteur stocké dans vecteur_jeux)"""
	
	vect_u = [0 for i in range (len(vecteur_jeux[0]))]	#Vecteur barycentre de joueur
	if uTot == 0 :
		return vect_u
	
	for i in range (len(vecteur_jeux)) :	#Pour chaque jeu
		
		for j in range (len(vecteur_jeux[0])):	#Pour chaque composante du vecteur
			vect_u[j] += vecteur_jeux[i][j] * nb_jeux_joues[joueur][i] / uTot
		
	return vect_u


def valeurHypp( dist : float, distmax : float, distmin : float, umax : int) :
	"""Hypothèse: distmax > dist > distmin"""
	"""Donne une valeur hypothétique de j pour X"""
	assert distmax >= dist >= distmin
	
	return umax*(dist-distmin)/(distmax-distmin)



def contenus(nb_jeux_joues :list , vecteur_jeux : list, joueur : int, nb_jeux_jouee_par_joueur : int) :
	"""Renvoie un tableau des notes hypothétiques pour joueur pour les jeux non joués de nb_jeux_joues de taille n x m, les jeux sont représentés par des vecteurs de taille nx dans vecteur_jeux"""
	assert len(nb_jeux_joues[0]) == len(vecteur_jeux)
	m = len(vecteur_jeux)
	notes = [ 0 for i in range (m) ]
	dist = [ 0. for i in range (m) ]
	
	vect_u = barycentre(nb_jeux_joues,vecteur_jeux,joueur, nb_jeux_jouee_par_joueur)	#barycentre
	
	distmax = 0.0
	distmin = float('inf')
	umax = 0
	
	
	for i in range (m):	#On calcule les distances au barycentre

		dist[i] = distance(vecteur_jeux[i], vect_u)
		
		if dist[i] > distmax :
			distmax = dist[i]
			umax = nb_jeux_joues[joueur][i]
			
		if dist[i] < distmin :
			distmin = dist[i]
	
	
	for i in range (m):	#On donne les notes
		
		notes[i] = valeurHypp(dist[i], distmax, distmin, umax)
	
	return notes
