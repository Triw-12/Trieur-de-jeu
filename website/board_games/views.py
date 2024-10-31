from django.shortcuts import render

def home(request):
    return render(request, 'board_games/home.html')

def advanced_search(request):
    return render(request, 'board_games/advanced_search.html')

def add_game(request):
    return render(request, 'board_games/add_game.html')
