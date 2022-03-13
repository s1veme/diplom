# Generated by Django 3.1 on 2022-03-10 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20220310_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='group',
            name='visit_type',
            field=models.CharField(blank=True, choices=[('remote', 'Удаленная'), ('locale', 'Очная')], default='none', max_length=10, null=True, verbose_name='Тип группы'),
        ),
    ]