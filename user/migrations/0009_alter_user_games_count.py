# Generated by Django 3.2 on 2021-05-19 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_user_games_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='games_count',
            field=models.IntegerField(default=5),
        ),
    ]