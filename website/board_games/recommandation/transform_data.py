from board_games.models import Games, Tags, History, History_players, Rating
from authentification.models import User
		


def games_to_vector():
    """
    Crée un vecteur de jeux à partir de la base de données
    """
    games = Games.objects.all()
    games_vector = []
    for game in games:
        tags_ = Tags.objects.filter(game_id=game)
        tags_link = {
            "Chance" : (0, 1/6),
            "Adresse" : (0, 3/6),
            "Réflexion" : (0, 5/6),
            "Stratégie" : (0, 6/6),
            "Cartes" : (4, 0),
            "Plateau" : (4, 1/3),
            "Dés": (4, 2/3),
            "AE": (4, 3/3),
            "Coop": (5, 0),
            "Team VS": (5, 1/2),
            "VS": (5, 2/2),
            "Bluff" : (6, 1),
            "Conquête" : (7, 1),
            "Déduction" : (8, 1),
            "Construction" : (9, 1),
            "Improvisation" : (10, 1),
            "Mémoire" : (11, 1),
            "Rôle Caché": (12, 1),
            "Rigolo": (13, 1),
            "RP": (14, 1),
        }
        tags = [0 for _ in range(15)]
        tags[1] = game.game_length_max
        tags[2] = game.min_age
        tags[3] = game.difficulty
        for tag in tags_:
            if tag.tag_id in tags_link:
                tags[tags_link[tag.tag_id][0]] = tags_link[tag.tag_id][1]
            else:
                print("Tag non reconnu : ", tag.tag_id)
        #Ordre : Type (Adresse Chance Reflexion Stratégie), Durée, Age, Difficulté, Matériel (Carte, Plateau, Dés, AE), Équipe (Coop, VS, Team VS), Autre tags (tableau de 9 pour l'instant)) 
        games_vector.append(tags)
        
        
    return games_vector


def user_game_stats():
    """
    Renvoie deux matrices :
    - nb_jeux_joues : la première composante est le joueur, la deuxième est un jeu, la case contient le nombre de fois que le joueur a joué au jeu
    - listvote : la première composante est le joueur, la deuxième est un jeu, la case contient le vote du joueur pour le jeu
    Ainsi qu'un dictionnaire dict_user qui mappe l'id utilisateur à l'indice de la matrice.
    """
    users = User.objects.all()
    games = Games.objects.all()
    dict_user = {}
    nb_jeux_joues = [[0 for _ in range(len(games))] for _ in range(len(users))]
    listvote = [[0 for _ in range(len(games))] for _ in range(len(users))]
    for i, user in enumerate(users):
        history_players = History_players.objects.filter(user_id=user)
        dict_user[user.id] = i
        for history_player in history_players:
            history = history_player.play_id
            game = history.game_id
            nb_jeux_joues[i][game.game_id-1] += 1

            rating = Rating.objects.filter(user_id=user, game_id=game).first()
            if rating is not None:
                listvote[i][game.game_id-1] = rating.rating
            else:
                listvote[i][game.game_id-1] = 0
    return nb_jeux_joues, listvote, dict_user
