from django.shortcuts import render, redirect
from board_games import forms
from board_games.models import Games

def home(request):
    simple_search = forms.Simple_search()
    return render(request, 'board_games/home.html', context={'simple_search': simple_search})

def advanced_search(request):
    simple_search = forms.Simple_search()
    form = forms.Advanced_search()
    if request.method == 'POST':
        form = forms.Advanced_search(request.POST)
        simple_search = forms.Simple_search()
        if form.is_valid():
            games = Games.objects.all()
            if form.cleaned_data['game_name']:
                games = games.filter(game_name__icontains=form.cleaned_data['game_name'])
            if form.cleaned_data['min_players']:
                games = games.filter(min_players__gte=form.cleaned_data['min_players'])
            if form.cleaned_data['max_players']:
                games = games.filter(max_players__lte=form.cleaned_data['max_players'])
            if form.cleaned_data['min_age']:
                games = games.filter(min_age__gte=form.cleaned_data['min_age'])
            if form.cleaned_data['game_length_min']:
                games = games.filter(game_length_min__gte=form.cleaned_data['game_length_min'])
            if form.cleaned_data['game_length_max']:
                games = games.filter(game_length_max__lte=form.cleaned_data['game_length_max'])
            if form.cleaned_data['tag']:
                games = games.filter(tag__icontains=form.cleaned_data['tag'])
            return render(request, 'board_games/advanced_search.html', context={'form': form, 'simple_search': simple_search, 'games': games})
        elif simple_search.is_valid():
            games = Games.objects.filter(game_name__icontains=simple_search.cleaned_data['game_name'])
            return render(request, 'board_games/advanced_search.html', context={'form': form, 'simple_search': simple_search, 'games': games})
    return render(request, 'board_games/advanced_search.html', context={'form': form, 'simple_search': simple_search})

def add_game(request):
    simple_search = forms.Simple_search()
    form = forms.AddGames()
    if request.method == 'POST':
        form = forms.AddGames(request.POST)
        if form.is_valid():
            game = form.save()
            return redirect('home')
    return render(request, 'board_games/add_game.html',context={'form': form, 'simple_search': simple_search})

def game(request, id):
    simple_search = forms.Simple_search()
    game = Games.objects.get(game_id=id)
    return render(request, 'board_games/game.html', context={'game': game, 'simple_search': simple_search})