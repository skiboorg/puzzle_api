# Generated by Django 3.2 on 2021-04-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210421_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_ok',
        ),
        migrations.AddField(
            model_name='user',
            name='wechatid',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='wechatid'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user/avatars', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Эл. почта'),
        ),
    ]
