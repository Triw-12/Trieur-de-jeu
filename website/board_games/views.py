from django.shortcuts import render, redirect
from board_games import forms
from board_games.models import Games, Tags, History, History_players, Rating
from board_games.recommandation.hybride import notes
from authentification.models import User
from datetime import datetime
from django.http import HttpResponseForbidden, HttpResponseNotFound


def home(request):
    simple_search = forms.Simple_search()
    games = None
    if request.user.is_authenticated:
        games = Games.objects.all()
        notes_game = notes(request.user.id)
        games = sorted([(game, notes_game[i]) for i, game in enumerate(games)], key=lambda x: x[1], reverse=True)[:15]
    return render(request, 'board_games/home.html', context={'simple_search': simple_search, 'games': games})

def advanced_search(request):
    simple_search = forms.Simple_search()
    form = forms.Advanced_search()
    if request.method == 'POST':
        form = forms.Advanced_search(request.POST)
        simple_search = forms.Simple_search()
        if form.is_valid():
            tags = Tags.objects.all()
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
            games_and_tags = {}
            for tag in tags:
                if tag.game_id in games:
                    if tag.game_id not in games_and_tags:
                        games_and_tags[tag.game_id] = ""
                    games_and_tags[tag.game_id] += tag.tag_id + ", " 
            for key in games_and_tags.keys():
                games_and_tags[key] = games_and_tags[key][:-2]
            return render(request, 'board_games/advanced_search.html', context={'form': form, 'simple_search': simple_search, 'games': games_and_tags})
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
    rating = forms.RateGame()
    game = Games.objects.get(game_id=id)
    users = User.objects.all()
    message = ""
    if 'rated' in request.GET:
        message = "Merci pour votre évaluation!"
    if request.method == 'POST':
        num_players = request.POST.get('num_players')
        if num_players:
            history = History.objects.create(game_id=game, date=datetime.now())
            for i in range(int(num_players)):
                user = request.POST.get('player_' + str(i+1))
                if user:
                    user_db = User.objects.get(id=user)
                    History_players.objects.create(play_id=history, user_id=user_db)
                    message = 'Partie enregistrée'
    return render(request, 'board_games/game.html', context={'game': game, 'simple_search': simple_search, 'users': users, 'message': message, 'form': rating})

def profil(request, id):
    simple_search = forms.Simple_search()
    if request.user.id != id and not request.user.is_superuser:
        return HttpResponseForbidden()
    user = User.objects.get(id=id)
    return render(request, 'board_games/profil.html', context={'user': user, 'simple_search': simple_search})

def stats(request):
    simple_search = forms.Simple_search()
    users = User.objects.all()
    return render(request, 'board_games/stats.html', context={'users': users, 'simple_search': simple_search})

def rate_game(request,id):
    form = forms.RateGame()
    game = Games.objects.get(game_id=id)
    if request.method == 'POST':
        form = forms.RateGame(request.POST)
        if form.is_valid():
            existing_rating = Rating.objects.filter(game_id=game, user_id=request.user).first()
            if existing_rating:
                existing_rating.delete()
            rating = form.save(commit=False)
            rating.game_id = game
            rating.user_id = request.user
            rating.save()
            return redirect(f'../game/{id}?rated={rating.rating}')
    return HttpResponseNotFound