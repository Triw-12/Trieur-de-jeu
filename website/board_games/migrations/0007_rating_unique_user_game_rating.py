# Generated by Django 5.1.1 on 2025-01-16 10:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_games', '0006_remove_history_rating_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.UniqueConstraint(fields=('user_id', 'game_id'), name='unique_user_game_rating'),
        ),
    ]
