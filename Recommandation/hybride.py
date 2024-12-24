from collaboratif import collaboratif
from contenus import contenus

def notes(nb_jeux_joues : list, vecteur_jeux : list, u : int) :
	"""Hypothèse : nb_jeux_joues est de dimension n*m, vecteur_jeux est de taille nx, u<m"""
	"""Renvoie les notes hypothétiques des jeux pour u conformément au donné de nb_jeux_joues et vecteur_jeux"""
	m = len(vecteur_jeux)
	uMoy : int = sum(nb_jeux_joues[u]) / m
	uTot : int = sum(nb_jeux_joues[u])

	notesCollaboratif = collaboratif(nb_jeux_joues,u)
	notesContenus = contenus(nb_jeux_joues,vecteur_jeux,u,uTot)

	notes = [ (notesCollaboratif[i] + notesContenus[i]) /2 for i in range (m) ]
	
	return notes


