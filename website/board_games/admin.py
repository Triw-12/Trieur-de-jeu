from django.contrib import admin
from board_games.models import Games, Lending, Tags, History, History_players, Extensions, Rating


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    readonly_fields = ('game_id',)
    list_display = ('game_name', 'stock_nb', 'game_length_min', 'game_length_max', 'min_players', 'max_players', 'min_age', 'difficulty')
    list_filter = ('difficulty', 'min_age', 'max_players')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    readonly_fields = ('tag_id',)
    list_display = ('game_id', 'tag_id')
    list_filter = ('game_id',)


@admin.register(Lending)
class LendingAdmin(admin.ModelAdmin):
    readonly_fields = ('lending_id',)
    list_display = ('user_id', 'game_id', 'date_start', 'date_expected_end', 'date_end')
    list_filter = ('date_start', 'date_expected_end', 'date_end')


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    readonly_fields = ('play_id',)
    list_display = ('game_id', 'date')
    list_filter = ('date',)

@admin.register(History_players)
class HistoryPlayersAdmin(admin.ModelAdmin):
    readonly_fields = ('play_id', 'user_id')
    list_display = ('play_id', 'user_id')
    list_filter = ('play_id', 'user_id')

@admin.register(Extensions)
class ExtensionsAdmin(admin.ModelAdmin):
    readonly_fields = ('extension_id',)
    list_display = ('extension_name', 'game_id', 'time_add')
    list_filter = ('game_id',)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('rating_id',)
    list_display = ('user_id', 'game_id', 'rating')
    list_filter = ('rating', 'game_id', 'user_id')