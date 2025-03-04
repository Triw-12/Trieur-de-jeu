from django.db import models
from django.contrib.auth.models import AbstractUser
from board_games.models import History_players, Rating, History

class User(AbstractUser):
    first_name = None
    last_name = None

    def nb_games_played(self):
        return History_players.objects.filter(user_id=self).count()
    
    def nb_games_played_unique(self):
        return History.objects.filter(play_id__in=History_players.objects.filter(user_id=self)).count()
    
    def nb_games_rated(self):
        return Rating.objects.filter(user_id=self).count()
    def avg_rating(self):
        ratings = Rating.objects.filter(user_id=self)
        if len(ratings) == 0:
            return 0
        return sum([rating.rating for rating in ratings]) / len(ratings)
    