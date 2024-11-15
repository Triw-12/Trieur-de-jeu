from django.shortcuts import render, redirect
from board_games import forms
from board_games.models import Games

def home(request):
    return render(request, 'board_games/home.html')

def advanced_search(request):
    return render(request, 'board_games/advanced_search.html')

def add_game(request):
    form = forms.AddGames()
    if request.method == 'POST':
        form = forms.AddGames(request.POST)
        if form.is_valid():
            game = form.save()
            return redirect('home')
    return render(request, 'board_games/add_game.html',context={'form': form})
