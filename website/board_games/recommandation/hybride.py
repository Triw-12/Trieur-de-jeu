from board_games.recommandation.collaboratifVote import collaboratif
from board_games.recommandation.contenusVote import contenus
from board_games.recommandation.transform_data import games_to_vector, user_game_stats


nb_jeux_joues = []
vecteur_jeux = []
dict_user = {}

def init():
	"""Initialise les données"""
	global nb_jeux_joues
	global vecteur_jeux
	global listvote
	global dict_user
	nb_jeux_joues, listvote, dict_user = user_game_stats()
	vecteur_jeux = games_to_vector()


def notes(user_id : int):
	"""Hypothèse : nb_jeux_joues est de dimension n*m, vecteur_jeux est de taille nx, joueur<m"""
	"""Renvoie les notes hypothétiques des jeux pour joueur conformément aux données de nb_jeux_joues et vecteur_jeux"""
	init()
	joueur : int = dict_user[user_id]
	m = len(vecteur_jeux)
	nb_total_joue : int = sum(nb_jeux_joues[joueur])

	notesCollaboratif = collaboratif(nb_jeux_joues,joueur, listvote)
	notesContenus = contenus(nb_jeux_joues,vecteur_jeux,joueur,nb_total_joue, listvote)

	notes = [ (notesCollaboratif[i] + notesContenus[i])/2 for i in range (m) ]
	
	return notes


