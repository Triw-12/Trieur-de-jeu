from django import forms
from board_games.models import Games, Extensions, Rating

class AddGames(forms.ModelForm):
    class Meta:
        model = Games
        fields = ['game_name', 'stock_nb', 'game_length_min', 'game_length_max', 'min_players', 'max_players', 'min_age']

class AddExtensions(forms.ModelForm):
    class Meta:
        model = Extensions
        fields = ['extension_name', 'time_add']


class Simple_search(forms.Form):
    game_name = forms.CharField(label='Nom du jeu', max_length=200, required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["game_name"].widget.attrs.update({
            "placeholder": "Nom du jeu",
            "size": "10%",
        })

class Advanced_search(forms.Form):
    game_name = forms.CharField(label='Nom du jeu', max_length=200, required=False)
    min_players = forms.IntegerField(label='Nombre de joueurs minimum', required=False)
    max_players = forms.IntegerField(label='Nombre de joueurs maximum', required=False)
    min_age = forms.IntegerField(label='Age minimum', required=False)
    game_length_min = forms.IntegerField(label='Durée minimum', required=False)
    game_length_max = forms.IntegerField(label='Durée maximum', required=False)
    tags = forms.CharField(label='Tag', max_length=200, required=False)

class RateGame(forms.ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 11)]
    
    rating = forms.ChoiceField(choices=RATING_CHOICES, label='Rating')
    
    class Meta:
        model = Rating
        fields = ['rating']
