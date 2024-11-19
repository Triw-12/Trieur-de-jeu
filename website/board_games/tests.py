from django.test import TestCase
from board_games.models import Games, Extensions, Tags, Lending, History, History_players
from authentification.models import User

class GameTestCase(TestCase):
    def setUp(self):
        self.game = Games.objects.create(game_name="Test game", game_length_min=10, game_length_max=20, min_players=2, max_players=4, min_age=10)
        self.extension = Extensions.objects.create(extension_name="Test extension", game_id=self.game , time_add=5)
        self.tag = Tags.objects.create(game_id=self.game, tag_id="Test tag")
        self.user = User.objects.create_user(username="test", password="test")
        self.lending = Lending.objects.create(user_id=self.user, game_id=self.game, date_start="2021-01-01", date_expected_end="2021-01-15")

    def test_game(self):
        game = Games.objects.get(game_name="Test game")
        extension = Extensions.objects.get(extension_name="Test extension")
        self.assertEqual(game.stock_nb, 1)
        self.assertEqual(extension.time_add, 5)

    def test_game_creation(self):
        self.assertEqual(self.game.stock_nb, 1)
        self.assertEqual(self.game.game_length_min, 10)
        self.assertEqual(self.game.game_length_max, 20)
        self.assertEqual(self.game.min_players, 2)
        self.assertEqual(self.game.max_players, 4)
        self.assertEqual(self.game.min_age, 10)

    def test_extension_creation(self):
        self.assertEqual(self.extension.extension_name, "Test extension")
        self.assertEqual(self.extension.time_add, 5)

    def test_tag_creation(self):
        self.assertEqual(self.tag.tag_id, "Test tag")

    def test_lending_creation(self):
        self.assertEqual(self.lending.game_id, self.game)
        self.assertEqual(self.lending.date_start, "2021-01-01")
        self.assertEqual(self.lending.date_expected_end, "2021-01-15")

    
