from django.test import TestCase

from board_games.views import *

class ViewsTest(TestCase) :
	
	def setUp(self) :
		self.game = Games.objects.create(game_name="Test game", game_length_min=10, game_length_max=20, min_players=2, max_players=4, min_age=10, difficulty=3)
		Tags.objects.create(game_id=self.game, tag_id="Test tag1")
		Tags.objects.create(game_id=self.game, tag_id="Test tag2")
   
	def test_get_game_tags(self) :
		dico = get_game_tags(Games.objects.all())
		self.assertEqual(dico[self.game], "Test tag1, Test tag2")


	def test_home(self) :
		response = self.client.get('htmlcov/index.html')
		print(response)
