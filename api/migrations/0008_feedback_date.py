# Generated by Django 3.2 on 2021-04-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
