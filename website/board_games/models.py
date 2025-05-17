from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Games(models.Model):
    game_id = models.AutoField("game_id", primary_key=True, blank=False)
    game_name = models.CharField("game_name", unique=True, max_length=200, blank=False)
    stock_nb = models.IntegerField("stock_nb", default=1, blank=True)
    game_length_min = models.IntegerField("game_length_min", default=0, blank=True)
    game_length_max = models.IntegerField("game_length_max", default=999, blank=True)
    min_players = models.IntegerField("min_players", default=1, blank=True)
    max_players = models.IntegerField("max_players", default=99, blank=True)
    min_age = models.IntegerField("min_age", default=0, blank=True)
    difficulty = models.IntegerField("difficulty", default=1, blank=False, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.game_name
    
    def rating(self):
        ratings = Rating.objects.filter(game_id=self.pk)
        if not ratings.exists():
            return 0
        return sum(rating.rating for rating in ratings) / ratings.count()

class Lending(models.Model):
    lending_id = models.AutoField(primary_key=True, blank=False)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    game_id = models.ForeignKey(Games,blank=False,on_delete=models.CASCADE)
    date_start = models.DateField("date_start", blank=False)
    date_expected_end = models.DateField("date_end", blank=False)
    date_end = models.DateField("date_end", blank=True, null=True)

    def __str__(self):
        return '(' + str(self.user_id) + ', ' + str(self.game_id) + ')'

class Tags(models.Model):
    game_id = models.ForeignKey(Games,blank=False, on_delete=models.CASCADE)
    tag_id = models.CharField("tag_id", max_length=200, blank=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['game_id', 'tag_id'], name='unique_migration_host_combination_tags'
            )
        ]
    def __str__(self):
        return '(' + str(self.game_id) + ', ' + str(self.tag_id) + ')'


class History(models.Model):
    play_id = models.AutoField("play_id", primary_key=True, blank=False)
    game_id = models.ForeignKey(Games,blank=False, on_delete=models.CASCADE)
    date = models.DateTimeField("date", auto_now_add=True)

    def __str__(self):
        return '(' + str(self.game_id) + ', ' + str(self.date) + ')'

class History_players(models.Model):
    play_id = models.ForeignKey(History,blank=False,on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,blank=False,on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['play_id', 'user_id'], name='unique_migration_host_combination_history'
            )
        ]

    def __str__(self):
        return '(' + str(self.play_id) + ', ' + str(self.user_id) + ')'

class Extensions(models.Model):
    extension_id = models.AutoField("extension_id", primary_key=True, blank=False)
    extension_name = models.CharField("extension_name", unique=True, max_length=200, blank=False)
    game_id = models.ForeignKey(Games,blank=False,on_delete=models.CASCADE)
    time_add = models.IntegerField("time_add", blank=False)

    def __str__(self):
        return self.extension_name + " of " + self.game_id.game_name

class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True, blank=False)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    game_id = models.ForeignKey(Games,blank=False,on_delete=models.CASCADE)
    rating = models.IntegerField("rating", blank=False, validators=[MinValueValidator(1), MaxValueValidator(10)])
    date = models.DateTimeField("date", auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_id', 'game_id'], name='unique_user_game_rating'
            )
        ]

    def __str__(self):
        return '(' + str(self.user_id) + ', ' + str(self.game_id) + ', ' + str(self.rating) + ')'