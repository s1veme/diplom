# Generated by Django 3.2 on 2022-03-17 03:21

import departments.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_department_manager_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='basic_timetable_department',
            field=models.FileField(blank=True, null=True, upload_to='timetable-d/', validators=[departments.validators.validate_file_extension], verbose_name='Основное рассписание'),
        ),
        migrations.AlterField(
            model_name='department',
            name='session_timetable_department',
            field=models.FileField(blank=True, null=True, upload_to='timetable-d/', validators=[departments.validators.validate_file_extension], verbose_name='Рассписание сессии'),
        ),
    ]
