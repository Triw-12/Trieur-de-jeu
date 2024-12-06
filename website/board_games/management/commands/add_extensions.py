import os
import django
import csv
from django.core.management.base import BaseCommand

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from board_games.models import Games, Extensions
from django.conf import settings


class Command(BaseCommand):
    help = 'Add extensions to the database from a CSV file.'
    # Get all extension names

    def handle(self, *args, **options):
        
        extension_name_list = Extensions.objects.values_list('extension_name', flat=True).distinct()

        # Open Jeu_csv-Extentions.csv in read-only mode using csv.reader.
        file_path = os.path.join(settings.BASE_DIR, 'static', 'csv/Jeu_csv-Extentions.csv')
        with open(file_path, "r") as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)  # Skip the header row
            for row in reader:
                extension_name, game_name, time_add = row
                # Change game_name in order to escape the ' symbol in SQL.

                try:
                    game = Games.objects.get(game_name=game_name)
                except Games.DoesNotExist:
                    print(f"Game '{game_name}' does not exist in the database.")
                    continue

                if extension_name not in extension_name_list:  # If the game is not yet in the database
                    # Then add it to the database
                    Extensions.objects.create(time_add=time_add, game_id=game, extension_name=extension_name)
                    extension_name_list = Extensions.objects.values_list('extension_name', flat=True).distinct()
        print("Extensions added to the database.")
