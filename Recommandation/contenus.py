from math import *

def distance(v1: list, v2: list) :
	"""Renvoie la distance entre v1 et v2, tous deux de même tailles"""
	assert len(v1) == len(v2)
	dist : int = 0
	
	for i in range (len(v1)) :
		dist += (v1[i] - v2[i])**2
	
	dist = sqrt(dist)
	return dist


def barycentre(nb_jeux_joues: list, vecteur_jeux : list, u: int, uTot : int) :
	"""Calcule le barycentre de u par rapport au jeu de nb_jeux_joues (sous la forme de vecteur stocké dans vecteur_jeux)""" 
	
	vect_u = [0 for i in range (len(vecteur_jeux[0]))]	#Vecteur barycentre de u
	
	for i in range (len(vecteur_jeux)) :	#Pour chaque jeu
		
		for j in range (len(vecteur_jeux[0])):	#Pour chaque composante du vecteur
			vect_u[j] += vecteur_jeux[i][j] * nb_jeux_joues[u][i] / uTot
		
	return vect_u


def valeurHypp( dist : float, distmax : float, distmin : float, utot : int) :
	"""Hypothèse: distmax > dist > distmin"""
	"""Donne une valeur hyppotétique de j pour X"""
	assert distmax > dist > distmin
	
	return utot*(dist-distmin)/(distmax-distmin)



def contenus(nb_jeux_joues :int , vecteur_jeux : list, u : int, utot : int) :
	"""Renvoie un tableau des notes hypothétiques pour u pour les jeux non joués de nb_jeux_joues de taille n x m, les jeux sont représentés par des vecteurs de taille nx dans vecteur_jeux"""
	assert len(nb_jeux_joues) == len(vecteur_jeux[0])
	m = len(vecteur_jeux)
	notes = [ 0 for i in range (m) ]
	dist = [ 0. for i in range (m) ]
	
	vect_u = barycentre(nb_jeux_joues,vecteur_jeux,u, utot)	#barycentre
	
	distmax = 0;
	distmin = 0;
	
	for i in range (m):	#On calcule les distances au barycentre
		
		dist[i] = distance(vecteur_jeux[i], vect_u)
		
		if nb_jeux_joues[u][i] > 0 and dist[i] > distmax :
			distmax = dist[i]
			
		elif nb_jeux_joues[u][i] > 0 and dist[i] < distmin :
			distmin = dist[i]
	
	
	for i in range (m):	#On donne les notes
		
		if nb_jeux_joues[u][i] == 0 :	#Si le jeu n'a jamais été joué
			notes[i] = valeurHypp(dist[i], distmax, distmin, utot)
	
	return notes
