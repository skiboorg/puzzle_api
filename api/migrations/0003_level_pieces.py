# Generated by Django 3.2 on 2021-04-21 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_game_game_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='pieces',
            field=models.IntegerField(default=0, verbose_name='Частей пазла'),
        ),
    ]