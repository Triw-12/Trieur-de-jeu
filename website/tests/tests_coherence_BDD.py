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
    
    