from django.db import models

from utils.model_utils import generate_id


class Department(models.Model):
    """Кафедры"""
    id = models.CharField(primary_key=True, max_length=10, unique=True, default=generate_id)
    name = models.CharField('Название кафедры', max_length=150, blank=True, null=True)
    email = models.CharField('Почта', max_length=50)
    phone_number = models.CharField('Номер телефона', max_length=50)
    address = models.CharField('Адрес', max_length=100)
    manager_department = models.OneToOneField(
        'profiles.Profile',
        related_name='manager_department',
        verbose_name="Заведущий кафедры",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    description = models.TextField('Описание')
    basic_timetable_department = models.FileField('Основное рассписание', upload_to='timetable-d/')
    session_timetable_department = models.FileField('Рассписание сессии', upload_to='timetable-d/')
    session_absentia_timetable_department = models.FileField('Рассписание сессии заочно', upload_to='timetable-d/')
    photo = models.ImageField('Фотография', upload_to='department/')
    photos = models.ImageField('Фотографии', upload_to='department/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"
