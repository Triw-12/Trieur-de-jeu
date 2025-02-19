from board_games.models import Games, Tags, History, History_players
from authentification.models import User


def games_to_vector():
    """
    Crée un vecteur de jeux à partir de la base de données
    """
    games = Games.objects.all()
    games_vector = []
    for game in games:
        tags = Tags.objects.filter(game_id=game)
        tags_list = [tag.tag_id for tag in tags]
        games_vector.append((game.difficulty, game.game_length_max, game.min_age, game.max_players))
    return games_vector


def number_play():
    """
    Renvoie une matrice dont la première composante et le joueur, la deuxième composante est un jeu et la case contient le nombre de fois que le joueur a joué au jeu
    """
    users = User.objects.all()
    games = Games.objects.all()
    dict_user = {}
    nb_jeux_joues = [[0 for _ in range(len(games))] for _ in range(len(users))]
    for i, user in enumerate(users):
        history_players = History_players.objects.filter(user_id=user)
        dict_user[user.id] = i
        for history_player in history_players:
            history = history_player.play_id
            game = history.game_id
            nb_jeux_joues[i][game.game_id-1] += 1
    return nb_jeux_joues, dict_user

