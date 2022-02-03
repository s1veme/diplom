# Generated by Django 3.1 on 2022-02-03 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        ('speciality', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='headmen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='headmen', to=settings.AUTH_USER_MODEL, verbose_name='Староста'),
        ),
        migrations.AddField(
            model_name='group',
            name='spec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Speciality', to='speciality.speciality', verbose_name='Специальность'),
        ),
    ]
