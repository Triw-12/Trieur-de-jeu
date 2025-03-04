from django.test import TestCase
from django.core.management import call_command

from board_games.models import *
from authentification.models import *

class TestCoherenceBDD(TestCase):

    @classmethod
    def setUpTestData(cls):
        call_command('add_games')
        call_command('add_extensions')

    def setUp(self):

        self.games = Games.objects.all()
        self.tags = Tags.objects.all()
        self.extensions = Extensions.objects.all()
    
    def test_imported_games(self):
        self.assertTrue(self.games.exists())
        self.assertTrue(self.tags.exists())
        self.assertTrue(self.extensions.exists())

    def test_unique_tags_per_game(self):
        valid_tags1 = {'Réflexion', 'Stratégie', 'Chance', 'Adresse'}
        valid_tags2 = {'Cartes', 'Plateau', 'Dés', 'AE'}
        valid_tags3 = {'Coop', 'Team VS', 'VS'}
        for game in self.games:
            tags = self.tags.filter(game_id=game)
            tag_names = {tag.tag_id for tag in tags}
            self.assertEqual(len(tag_names), len(tags))
            self.assertEqual(sum(tag in valid_tags1 for tag in tag_names), 1, f"Game '{game.game_name}' has invalid tags: {tag_names}")
            self.assertEqual(sum(tag in valid_tags2 for tag in tag_names), 1, f"Game '{game.game_name}' has invalid tags: {tag_names}")
            self.assertEqual(sum(tag in valid_tags3 for tag in tag_names), 1, f"Game '{game.game_name}' has invalid tags: {tag_names}")

    def test_no_duplicate_games(self):
        game_names = self.games.values_list('game_name', flat=True)
        self.assertEqual(len(game_names), len(set(game_names)), "There are duplicate games in the database")

    def test_game_fields_not_empty(self):
        for game in self.games:
            self.assertTrue(game.game_name, f"Game ID '{game.game_name}' has an empty name")
    
    def test_game_stock_positive(self):
        for game in self.games:
            self.assertGreaterEqual(game.stock_nb, 0, f"Game '{game.game_name}' has a negative stock number")

    def test_game_length_valid(self):
        for game in self.games:
            self.assertGreaterEqual(game.game_length_min, 0, f"Game '{game.game_name}' has a negative minimum length")
            self.assertLessEqual(game.game_length_max, 999, f"Game '{game.game_name}' has a maximum length greater than 999")
            self.assertLessEqual(game.game_length_min, game.game_length_max, f"Game '{game.game_name}' has a minimum length greater than maximum length")

    def test_player_count_valid(self):
        for game in self.games:
            self.assertGreaterEqual(game.min_players, 1, f"Game '{game.game_name}' has less than 1 minimum player")
            self.assertLessEqual(game.max_players, 99, f"Game '{game.game_name}' has more than 99 maximum players")
            self.assertLessEqual(game.min_players, game.max_players, f"Game '{game.game_name}' has a minimum player count greater than maximum player count")

    def test_game_difficulty_valid(self):
        for game in self.games:
            self.assertGreaterEqual(game.difficulty, 1, f"Game '{game.game_name}' has a difficulty less than 1")
            self.assertLessEqual(game.difficulty, 5, f"Game '{game.game_name}' has a difficulty greater than 5")

    def test_lending_dates(self):
        lendings = Lending.objects.all()
        for lending in lendings:
            self.assertLessEqual(lending.date_start, lending.date_expected_end, f"Lending '{lending.lending_id}' has a start date after the expected end date")
            if lending.date_end:
                self.assertLessEqual(lending.date_start, lending.date_end, f"Lending '{lending.lending_id}' has a start date after the end date")

    def test_rating_values(self):
        ratings = Rating.objects.all()
        for rating in ratings:
            self.assertGreaterEqual(rating.rating, 1, f"Rating '{rating.rating_id}' has a value less than 1")
            self.assertLessEqual(rating.rating, 10, f"Rating '{rating.rating_id}' has a value greater than 10")
