# Generated by Django 5.0.2 on 2024-03-11 06:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movie", "0006_review_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="genre",
            name="slug",
            field=models.SlugField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
