# Generated by Django 3.1 on 2022-03-10 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20220310_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='visit_type',
            field=models.CharField(choices=[('remote', 'Удаленная'), ('locale', 'Очная')], default='locale', max_length=10, verbose_name='Тип группы'),
        ),
    ]