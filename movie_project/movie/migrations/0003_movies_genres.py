# Generated by Django 5.0.2 on 2024-02-14 03:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movie", "0002_genre"),
    ]

    operations = [
        migrations.AddField(
            model_name="movies",
            name="genres",
            field=models.ManyToManyField(to="movie.genre"),
        ),
    ]
