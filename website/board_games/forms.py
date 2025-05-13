from django import forms
from board_games.models import Games, Extensions, Rating

class AddGames(forms.ModelForm):
    class Meta:
        model = Games
        fields = ['game_name', 'stock_nb', 'game_length_min', 'game_length_max', 'min_players', 'max_players', 'min_age']
        widgets = {
            'game_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du jeu'}),
            'stock_nb': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock disponible'}),
            'game_length_min': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Durée minimum (min)'}),
            'game_length_max': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Durée maximum (min)'}),
            'min_players': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre minimum de joueurs'}),
            'max_players': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre maximum de joueurs'}),
            'min_age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Âge minimum'}),
        }

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
    tags = forms.CharField(label='Tags', max_length=200, required=False)
    sort_by = forms.CharField(label='Trier par', required=True)

class RateGame(forms.ModelForm):
    RATING_CHOICES = [(i, '★' * i) for i in range(1, 11)]
    
    rating = forms.ChoiceField(
        choices=RATING_CHOICES, 
        label='Note', 
        widget=forms.RadioSelect(),
        initial=1
    )
    
    class Meta:
        model = Rating
        fields = ['rating']