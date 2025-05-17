from math import *


def distance(v1: list, v2: list) :
	"""Renvoie la distance entre v1 et v2, tous deux de même tailles"""
	assert len(v1) == len(v2)
	dist : float = 0
	
	for i in range (len(v1)) :
		
		if i < 2 :	#Pondération par rapport à l'importance du composant
			dist += (8 * (v1[i] - v2[i])) **2
		
		elif i < 6 :
			dist += (5 * (v1[i] - v2[i])) **2
		
		else :
			dist += (v1[i] - v2[i]) **2
	
	dist = sqrt(dist)
	return dist


def barycentre(nb_jeux_joues: list, vecteur_jeux : list, joueur: int, nb_total_jouer : int, listvote : list) :
	"""Calcule le barycentre de joueur par rapport au jeu de nb_jeux_joues (sous la forme de vecteur stocké dans vecteur_jeux)"""
	
	voteCoef : float = 0
	
	vect_u = [0 for i in range (len(vecteur_jeux[0]))]	#Vecteur barycentre de joueur
	if nb_total_jouer == 0 :
		return vect_u
	
	for i in range (len(vecteur_jeux)) :	#Pour chaque jeu
		
		if listvote[joueur][i] != 0 :
			voteCoef = listvote[joueur][i] * 2 / 10
		else :
			voteCoef = 1
		
		for j in range (len(vecteur_jeux[0])):	#Pour chaque composante du vecteur
			vect_u[j] += voteCoef* vecteur_jeux[i][j] * nb_jeux_joues[joueur][i] / nb_total_jouer
		
	return vect_u


def valeurHypp( dist : float, distmax : float, distmin : float, plus_joue : int) :
	"""Hypothèse: distmax > dist > distmin"""
	"""Donne une valeur hypothétique de j pour X"""
	assert distmax >= dist >= distmin
	
	if distmax == distmin :
		return plus_joue
	
	else :
		return plus_joue*(distmax-dist)/(distmax-distmin)



def contenus(nb_jeux_joues :list , vecteur_jeux : list, joueur : int, nb_jeux_jouee_par_joueur : int, listvote : list) :
	"""Renvoie un tableau des notes hypothétiques pour joueur pour les jeux non joués de nb_jeux_joues de taille n x m, les jeux sont représentés par des vecteurs de taille nx dans vecteur_jeux"""
	assert len(nb_jeux_joues[0]) == len(vecteur_jeux)
	m = len(vecteur_jeux)
	notes = [ 0 for i in range (m) ]
	dist = [ 0. for i in range (m) ]
	
	vect_u = barycentre(nb_jeux_joues,vecteur_jeux,joueur, nb_jeux_jouee_par_joueur, listvote)	#barycentre
	
	distmax = 0.0
	distmin = float('inf')
	plus_jouer = max(nb_jeux_joues[joueur])
	
	
	for i in range (m):	#On calcule les distances au barycentre

		dist[i] = distance(vecteur_jeux[i], vect_u)
		
		if dist[i] > distmax :
			distmax = dist[i]
			
		if dist[i] < distmin :
			distmin = dist[i]
	
	
	for i in range (m):	#On donne les notes
		
		notes[i] = valeurHypp(dist[i], distmax, distmin, plus_jouer)
	
	return notes
