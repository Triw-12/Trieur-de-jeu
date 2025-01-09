from collaboratif import collaboratif
from contenus import contenus
from transform_data import games_to_vector, nomber_play


nb_jeux_joues = []
vecteur_jeux = []

def init():
	"""Initialise les données"""
	global nb_jeux_joues
	global vecteur_jeux
	nb_jeux_joues = nomber_play()
	vecteur_jeux = games_to_vector()


def notes(u : int) :
	"""Hypothèse : nb_jeux_joues est de dimension n*m, vecteur_jeux est de taille nx, u<m"""
	"""Renvoie les notes hypothétiques des jeux pour u conformément au donné de nb_jeux_joues et vecteur_jeux"""
	m = len(vecteur_jeux)
	uMoy : int = sum(nb_jeux_joues[u]) / m
	uTot : int = sum(nb_jeux_joues[u])

	notesCollaboratif = collaboratif(nb_jeux_joues,u)
	notesContenus = contenus(nb_jeux_joues,vecteur_jeux,u,uTot)

	notes = [ (notesCollaboratif[i] + notesContenus[i]) /2 for i in range (m) ]
	
	return notes


