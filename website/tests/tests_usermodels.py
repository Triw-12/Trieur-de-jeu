from django.test import TestCase

from board_games.models import Games, Tags, History, History_players, Rating
from authentification.models import *

class ModelsTests(TestCase) :
	
	def setUp(self) :
		
		self.game = Games.objects.create(game_name="Test game", game_length_min=10, game_length_max=20, min_players=2, max_players=4, min_age=10, difficulty=3)
		Tags.objects.create(game_id=self.game, tag_id="RP")
		Tags.objects.create(game_id=self.game, tag_id="Test false tag")
		
		self.user = User.objects.create_user(username="test", password="test")
		
		self.history = History.objects.create(game_id=self.game)
		self.history_player = History_players.objects.create(play_id=self.history, user_id=self.user)

	
	def test_nb_games_played(self) :
		self.assertEqual(self.user.nb_games_played(), 1)

	def test_nb_games_played_unique(self) :
		self.assertEqual(self.user.nb_games_played_unique(), 1)
	
	def test_nb_games_rated(self) :
		self.assertEqual(self.user.nb_games_rated(), 0)

	def test_avg_rating(self) :
		self.assertEqual(self.user.avg_rating(), 0)
		
		Rating.objects.create(user_id = self.user,game_id = self.game, rating = 5)
		
		self.assertEqual(self.user.avg_rating(), 5)
