import os
import django
import csv

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from board_games.models import Games, Tags
from django.conf import settings
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = 'Add games to the database from a CSV file.'

    def handle(self, *args, **options):
        # Get all game names
        game_list = set(Games.objects.values_list('game_name', flat=True))

        # Open Jeu_csv-Jeux.csv in read-only mode.
        file_path = os.path.join(settings.BASE_DIR, 'static', 'csv/Jeu_csv-Jeux.csv')
        with open(file_path, "r") as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)  # Skip the header row

            for row in reader:
                game_name, difficulty, min_age, game_length_min, game_length_max, min_players, max_players, types, caution, stock_nb, present = row

                # If the game is not yet in the database
                if game_name not in game_list:
                    try:
                        # Add it to the database
                        game = Games.objects.create(
                            stock_nb=stock_nb,
                            game_length_min=game_length_min,
                            game_length_max=game_length_max,
                            min_players=min_players,
                            max_players=max_players,
                            min_age=min_age,
                            game_name=game_name
                        )

                        # Split the tags column into the different tags
                        tags = types.split("/")
                        # For each tag
                        for tag in tags:
                            # Add it to the corresponding table
                            Tags.objects.create(tag_id=tag, game_id=game)
                    except Exception as e:
                        print(f"Error inserting {game_name}: {e}")
