# Generated by Django 3.1 on 2022-03-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_auto_20220309_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.CharField(default='76b88b3771', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
