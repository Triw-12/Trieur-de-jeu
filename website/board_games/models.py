from django.db import models
from django.conf import settings


class Games(models.Model):
    game_id = models.AutoField("game_id", primary_key=True, blank=False)
    game_name = models.CharField("game_name", unique=True, max_length=200, blank=False)
    stock_nb = models.IntegerField("stock_nb", default=1, blank=True)
    game_length_min = models.IntegerField("game_length_min", default=0, blank=True)
    game_length_max = models.IntegerField("game_length_max", default=999, blank=True)
    min_players = models.IntegerField("min_players", default=1, blank=True)
    max_players = models.IntegerField("max_players", default=99, blank=True)
    min_age = models.IntegerField("min_age", default=0, blank=True)
    def save(self, *args, **kwargs):
        super(Games, self).save(*args, **kwargs)

class Lending(models.Model):
    lending_id = models.AutoField(primary_key=True, blank=False)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    game_id = models.ForeignKey(Games,blank=False,on_delete=models.CASCADE)
    date_start = models.DateField("date_start", blank=False)
    date_expected_end = models.DateField("date_end", blank=False)
    date_end = models.DateField("date_end", blank=True)

class Tags(models.Model):
    game_id = models.ForeignKey(Games,blank=False, on_delete=models.CASCADE)
    tag_id = models.CharField("tag_id", max_length=200, blank=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['game_id', 'tag_id'], name='unique_migration_host_combination_tags'
            )
        ]


class History(models.Model):
    play_id = models.AutoField("play_id", primary_key=True, blank=False)
    game_id = models.ForeignKey(Games,blank=False, on_delete=models.CASCADE)
    date = models.DateField("date", blank=False)
    rating = models.IntegerField("rating", blank=True)

class History_players(models.Model):
    play_id = models.ForeignKey(History,blank=False,on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,blank=False,on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['play_id', 'user_id'], name='unique_migration_host_combination_history'
            )
        ]

class Extensions(models.Model):
    extension_id = models.AutoField("extension_id", primary_key=True, blank=False)
    extension_name = models.CharField("extension_name", unique=True, max_length=200, blank=False)
    game_id = models.ForeignKey(Games,blank=False,on_delete=models.CASCADE)
    time_add = models.IntegerField("time_add", blank=False)