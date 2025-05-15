from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from board_games import forms
from board_games.models import Games, Tags, History, History_players, Rating, Extensions
from board_games.recommandation.hybride import notes

from authentification.models import User

from django.http import HttpResponseForbidden, HttpResponseNotFound
import logging
from os import listdir
from django.conf import settings
from django.db.models.functions import TruncDate


def get_game_tags(games):
    """Retourne un dictionnaire associant chaque jeu à ses tags sous forme de texte."""
    tags = Tags.objects.filter(game_id__in=[game.game_id for game in games])
    games_and_tags = {}

    for tag in tags:
        if tag.game_id not in games_and_tags:
            games_and_tags[tag.game_id] = ""
        games_and_tags[tag.game_id] += tag.tag_id + ", "

    # Retirer la virgule et l'espace en trop à la fin
    for key in games_and_tags.keys():
        games_and_tags[key] = games_and_tags[key][:-2]

    return games_and_tags


def home(request):
    simple_search = forms.Simple_search()
    favorite_games = []

    if request.user.is_authenticated:
        all_games = Games.objects.all()
        notes_game = notes(request.user.id)

        # Récupérer les 15 jeux préférés de l'utilisateur
        favorite_games = sorted(
            [(game, notes_game[i]) for i, game in enumerate(all_games)],
            key=lambda x: x[1],
            reverse=True
        )[:15]

        # Supprimer les notes, on ne garde que les jeux
        favorite_games = [game for game, _ in favorite_games]

    # Récupérer les jeux avec les tags spécifiques
    strategy_games = sorted(
        Games.objects.filter(tags__tag_id="Stratégie").distinct(),
        key=lambda game: game.rating() if hasattr(game, 'rating') else 0,
        reverse=True
    )
    reflexion_games = sorted(
        Games.objects.filter(tags__tag_id="Réflexion").distinct(),
        key=lambda game: game.rating() if hasattr(game, 'rating') else 0,
        reverse=True
    )
    luck_games = sorted(
        Games.objects.filter(tags__tag_id="Chance").distinct(),
        key=lambda game: game.rating() if hasattr(game, 'rating') else 0,
        reverse=True
    )
    dexterity_games = sorted(
        Games.objects.filter(tags__tag_id="Adresse").distinct(),
        key=lambda game: game.rating() if hasattr(game, 'rating') else 0,
        reverse=True
    )

    # Rassembler tous les jeux pour récupérer leurs tags
    all_displayed_games = set(favorite_games) | set(strategy_games) | set(reflexion_games) | set(luck_games) | set(dexterity_games)
    tags_game = get_game_tags(all_displayed_games)

    # Dictionnaire des images des jeux
    image_dict = get_image_dict(all_displayed_games)

    return render(request, 'board_games/home.html', {
        'simple_search': simple_search,
        'favorite_games': favorite_games,
        'strategy_games': strategy_games,
        'reflexion_games': reflexion_games,
        'luck_games': luck_games,
        'dexterity_games': dexterity_games,
        'tags_game': tags_game,
        'dict': image_dict
    })


def get_image_dict(games):
    """Helper function to get image paths for games."""
    image_dir_path = settings.BASE_DIR / "static/images/board_games" # Relative path to the images directory
    image_dir_path_website = "images/board_games" # Relative path to the images directory as seen by the website
    list_images = listdir(image_dir_path) # List all images in the images directory
    list_images_name_only = {image_name.split('.')[0]: image_name for image_name in list_images} # Dictionary linking the file name without it's extension it's full name.
    image_dict = {} # Dictionary containing the images path referenced by the game name

    for game in games:
        cleaned_game_name = ''.join(name_part for name_part in game.game_name if name_part.isalnum()) # Cleaning the game name
        image_filename = list_images_name_only.get(cleaned_game_name) # If a file with the game name is found, get it's full file name.

        if cleaned_game_name in list_images_name_only: # If a file with the game name is found
            image_dict[game.game_name] = f"{image_dir_path_website}/{image_filename}" # Then add it's proper path to image_dict.

    return image_dict # Return the dictionary containing the images.

def get_tags_id(tags, games):
    """Helper function to get tags for games."""
    # A optimiser si possible
    games_and_tags = {}
    for tag in tags:
        if tag.game_id in games:
            if tag.game_id not in games_and_tags:
                games_and_tags[tag.game_id] = ""
            games_and_tags[tag.game_id] += tag.tag_id + ", " 
    for key in games_and_tags.keys():
        games_and_tags[key] = games_and_tags[key][:-2]
    return games_and_tags

def advanced_search(request):
    simple_search = forms.Simple_search()
    form = forms.Advanced_search()
    tags = Tags.objects.all()
    tag_priorities = {
        "Chance": 1, "Adresse": 2, "Réflexion": 3, "Stratégie": 4,
        "Cartes": 5, "Plateau": 6, "Dés": 7, "AE": 8,
        "Coop": 9, "Team VS": 10, "VS": 11
    }

    tags_id = sorted(
        list(set(tag.tag_id for tag in tags)),
        key=lambda tag: tag_priorities.get(tag, float('inf'))
    )
    if request.method == 'POST':
        form = forms.Advanced_search(request.POST)
        simple_search = forms.Simple_search(request.POST)
        if form.is_valid():
            games = Games.objects.all()

            if form.cleaned_data['game_name']:
                games = games.filter(game_name__icontains=form.cleaned_data['game_name'])
            if form.cleaned_data['min_players']:
                games = games.filter(max_players__gte=form.cleaned_data['min_players'])
            if form.cleaned_data['max_players']:
                games = games.filter(min_players__lte=form.cleaned_data['max_players'])
            if form.cleaned_data['min_age']:
                games = games.filter(min_age__gte=form.cleaned_data['min_age'])
            if form.cleaned_data['game_length_min']:
                games = games.filter(game_length_min__gte=form.cleaned_data['game_length_min'])
            if form.cleaned_data['game_length_max']:
                games = games.filter(game_length_max__lte=form.cleaned_data['game_length_max'])
            if form.cleaned_data['tags']:
                tags_form = form.cleaned_data['tags'].split(',')
                game_filtered = tags.filter(tag_id__in=tags_form).values_list('game_id', flat=True).distinct()
                games = games.filter(game_id__in=game_filtered)

            sort_by = form.cleaned_data['sort_by']
            if sort_by:
                if sort_by == 'name':
                    games = games.order_by('game_name')
                elif sort_by == 'rating':
                    games = games.order_by('rating')
                elif sort_by == 'players_min':
                    games = games.order_by('min_players')
                elif sort_by == 'players_max':
                    games = games.order_by('max_players')
                elif sort_by == 'age_min':
                    games = games.order_by('min_age')
                elif sort_by == 'time_min':
                    games = games.order_by('game_length_min')
                elif sort_by == 'time_max':
                    games = games.order_by('game_length_max')
                elif sort_by == 'difficulty':
                    games = games.order_by('difficulty')
            
            games_and_tags = get_tags_id(tags, games)
            image_dict = get_image_dict(games)
            
            return render(request, 'board_games/advanced_search.html', context={'form': form, 'simple_search': simple_search, 'games': games, 'tags_game': games_and_tags, 'tags_id': tags_id, 'dict': image_dict})
        elif simple_search.is_valid():
            games = Games.objects.filter(game_name__icontains=simple_search.cleaned_data['game_name'])
            games_and_tags = get_tags_id(tags, games)
            image_dict = get_image_dict(games)
            return render(request, 'board_games/advanced_search.html', context={'form': form, 'simple_search': simple_search, 'games': games, 'tags_game': games_and_tags, 'tags_id': tags_id, 'dict': image_dict})

    return render(request, 'board_games/advanced_search.html', context={'form': form, 'simple_search': simple_search, 'tags_id': tags_id})

@login_required
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
    extensions = Extensions.objects.filter(game_id=game)
    users = User.objects.all()
    logger = logging.getLogger(__name__)
    error = False
    message = ""
    if 'rated' in request.GET:
        message = "Merci pour votre évaluation ! Vous avez donné la note de " + request.GET['rated'] + "/10"
    base_note = 1
    if request.user.is_authenticated:
        try:
            rating = Rating.objects.get(game_id=game, user_id=request.user)
        except Rating.DoesNotExist:
            base_note = 1
        else:
            base_note = rating.rating
    
    if request.method == 'POST':
        num_players = request.POST.get('num_players')
        if num_players and num_players.isdigit() and int(num_players) >= game.min_players and int(num_players) <= game.max_players:
            history = History.objects.create(game_id=game)
            added_users = set()
            for i in range(int(num_players)):
                user = request.POST.get('player_' + str(i+1))
                if user and user:
                    if user not in added_users:
                        try:
                            user_db = User.objects.get(username=user)
                        except User.DoesNotExist:
                            error = True
                            message = 'Un joueur n\'existe pas dans la base de données'
                            logger.error('Un joueur n\'existe pas dans la base de données: user_id=%s, game_id=%s', user, game.game_id)
                        else:
                            History_players.objects.create(play_id=history, user_id=user_db)
                            added_users.add(user)
                    else:
                        message = 'Un joueur a été ajouté plusieurs fois Merci de contacter un administrateur'
                        logger.error('Un joueur a été ajouté plusieurs fois: user_id=%s, game_id=%s', user, game.game_id)
                        error = True
            if not error:
                message = 'Partie enregistrée'
                logger.info('Partie enregistrée: game_id=%s, players=%s', game.game_id, list(added_users))
            else:
                History.objects.filter(play_id=history.play_id).delete()
        else:
            message = "Erreur dans le nombre de joueurs"
            logger.error('Erreur dans le nombre de joueurs: game_id=%s, num_players=%s, min_players=%s, max_players=%s', game.game_id, num_players, game.min_players, game.max_players)
    return render(request, 'board_games/game.html', context={'game': game, 'extensions': extensions, 'simple_search': simple_search, 'users': users, 'message': message, 'form': rating, 'base_note': base_note})

@login_required
def profil(request, id):
    simple_search = forms.Simple_search()
    user = User.objects.get(id=id)
    history_players = History_players.objects.filter(user_id=user)[:10]
    history = History.objects.filter(play_id__in=history_players.values_list('play_id', flat=True)).order_by('-date')
    
    # Grouper les parties par play_id et récupérer les utilisateurs ayant joué chaque partie
    parties = []
    for play_id in history.values_list('play_id', flat=True).distinct():
        play_history = History_players.objects.filter(play_id=play_id)
        players = User.objects.filter(id__in=play_history.values_list('user_id', flat=True))
        parties.append({
            'history': history.get(play_id=play_id),
            'players': players
        })
    print(parties)
    return render(request, 'board_games/profil.html', context={'user': user, 'simple_search': simple_search, 'parties': parties})

def stats(request):
    simple_search = forms.Simple_search()
    users = User.objects.annotate(date_joined_date=TruncDate('date_joined')).values('date_joined_date').distinct()
    user_data = {
        'labels': [],
        'data': []
    }
    cumulative_sum = 0
    for user in users:
        if user['date_joined_date']:
            user_data['labels'].append(user['date_joined_date'].strftime('%d/%m/%Y'))
            daily_count = User.objects.filter(date_joined__date=user['date_joined_date']).count()
            cumulative_sum += daily_count
            user_data['data'].append(cumulative_sum)

    games_plays = History.objects.annotate(play_date=TruncDate('date')).values('play_date').distinct()
    games_plays_data = {
        'labels': [],
        'data': []
    }
    cumulative_sum = 0
    for game_play in games_plays:
        if game_play['play_date']:
            games_plays_data['labels'].append(game_play['play_date'].strftime('%d/%m/%Y'))
            daily_count = History.objects.filter(date__date=game_play['play_date']).count()
            cumulative_sum += daily_count
            games_plays_data['data'].append(cumulative_sum)

    ratings = Rating.objects.annotate(rating_date=TruncDate('date')).values('rating_date').distinct()
    ratings_data = {
        'labels': [],
        'data': []
    }
    cumulative_sum = 0
    for rating in ratings:
        if rating['rating_date']:
            ratings_data['labels'].append(rating['rating_date'].strftime('%d/%m/%Y'))
            daily_count = Rating.objects.filter(date__date=rating['rating_date']).count()
            cumulative_sum += daily_count
            ratings_data['data'].append(cumulative_sum)

    if request.user.is_authenticated:
        user_games_plays = History.objects.filter(history_players__user_id=request.user).annotate(play_date=TruncDate('date')).values('play_date').distinct()
        user_games_plays_data = {
            'labels': [],
            'data': []
        }
        cumulative_sum = 0
        for game_play in user_games_plays:
            if game_play['play_date']:
                user_games_plays_data['labels'].append(game_play['play_date'].strftime('%d/%m/%Y'))
                daily_count = History.objects.filter(date__date=game_play['play_date'], history_players__user_id=request.user).count()
                cumulative_sum += daily_count
                user_games_plays_data['data'].append(cumulative_sum)

        user_ratings = Rating.objects.filter(user_id=request.user).annotate(rating_date=TruncDate('date')).values('rating_date').distinct()
        user_ratings_data = {
            'labels': [],
            'data': []
        }
        cumulative_sum = 0
        for rating in user_ratings:
            if rating['rating_date']:
                user_ratings_data['labels'].append(rating['rating_date'].strftime('%d/%m/%Y'))
                daily_count = Rating.objects.filter(date__date=rating['rating_date'], user_id=request.user).count()
                cumulative_sum += daily_count
                user_ratings_data['data'].append(cumulative_sum)

        return render(request, 'board_games/stats.html', context={
            'users': users,
            'simple_search': simple_search,
            'user_data': user_data,
            'games_plays_data': games_plays_data,
            'ratings_data': ratings_data,
            'user_games_plays_data': user_games_plays_data,
            'user_ratings_data': user_ratings_data
        })
    return render(request, 'board_games/stats.html', context={
            'users': users,
            'simple_search': simple_search,
            'user_data': user_data,
            'games_plays_data': games_plays_data,
            'ratings_data': ratings_data,
        })
                

@login_required
def rate_game(request,id):
    form = forms.RateGame()
    game = Games.objects.get(game_id=id)
    if request.method == 'POST':
        form = forms.RateGame(request.POST)
        if form.is_valid():
            existing_ratings = Rating.objects.filter(game_id=game, user_id=request.user)
            if existing_ratings.exists():
                existing_ratings.delete()
            rating = form.save(commit=False)
            rating.game_id = game
            rating.user_id = request.user
            rating.save()
            return redirect(f'/game/{id}?rated={rating.rating}')
    return HttpResponseNotFound()