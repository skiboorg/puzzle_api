# Generated by Django 3.2 on 2021-04-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_level_pieces'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ad/')),
                ('video', models.FileField(upload_to='ad/')),
            ],
        ),
    ]
