# Generated by Django 3.2 on 2021-04-25 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210424_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='balance',
            field=models.IntegerField(default=0, editable=False, verbose_name='+баланс в %'),
        ),
    ]
