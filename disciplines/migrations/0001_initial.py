# Generated by Django 3.2 on 2022-04-13 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Имя дисциплины')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.department', verbose_name='Кафедра')),
            ],
            options={
                'verbose_name': 'Дисциплина',
                'verbose_name_plural': 'Дисциплины',
            },
        ),
    ]
