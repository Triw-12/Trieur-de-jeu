from django import forms
from board_games.models import Games

class AddGames(forms.ModelForm):
    class Meta:
        model = Games
        fields = ['game_name', 'stock_nb', 'game_length_min', 'game_length_max', 'min_players', 'max_players', 'min_age']
