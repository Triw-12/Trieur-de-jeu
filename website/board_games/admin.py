from django.contrib import admin
from board_games.models import Games, Lending, Tags, History, History_players, Extensions


admin.site.register(Games)
admin.site.register(Tags)
admin.site.register(Lending)
admin.site.register(History)
admin.site.register(History_players)
admin.site.register(Extensions)

