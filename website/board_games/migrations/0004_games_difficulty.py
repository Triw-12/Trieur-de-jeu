# Generated by Django 5.1.1 on 2025-01-09 14:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_games', '0003_alter_history_rating_alter_lending_date_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='difficulty',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='difficulty'),
        ),
    ]
