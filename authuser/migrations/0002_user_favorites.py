# Generated by Django 4.2 on 2023-04-22 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("moves", "0014_alter_exercise_variation"),
        ("authuser", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="favorites",
            field=models.ManyToManyField(
                blank=True, related_name="favorited_by", to="moves.exercise"
            ),
        ),
    ]
