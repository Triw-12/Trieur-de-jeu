from board_games.recommandation.collaboratif import collaboratif
from board_games.recommandation.contenus import contenus
from board_games.recommandation.transform_data import games_to_vector, number_play


nb_jeux_joues = []
vecteur_jeux = []
dict_user = {}

def init():
	"""Initialise les données"""
	global nb_jeux_joues
	global vecteur_jeux
	global dict_user
	nb_jeux_joues, dict_user = number_play()
	vecteur_jeux = games_to_vector()


def notes(user_id : int):
	"""Hypothèse : nb_jeux_joues est de dimension n*m, vecteur_jeux est de taille nx, joueur<m"""
	"""Renvoie les notes hypothétiques des jeux pour joueur conformément aux données de nb_jeux_joues et vecteur_jeux"""
	init()
	joueur : int = dict_user[user_id]
	m = len(vecteur_jeux)
	uTot : int = sum(nb_jeux_joues[joueur])

	notesCollaboratif = collaboratif(nb_jeux_joues,joueur)
	notesContenus = contenus(nb_jeux_joues,vecteur_jeux,joueur,uTot)

	notes = [ (notesCollaboratif[i] + notesContenus[i]) /2 for i in range (m) ]
	
	return notes


