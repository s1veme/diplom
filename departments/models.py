from django.db import models
import uuid
from shortuuid.django_fields import ShortUUIDField

class Department(models.Model):
    """Кафедры"""
    id = ShortUUIDField(
        primary_key=True, length=10, unique=True, default=uuid.uuid4().hex[:10], editable=False
    )
    name = models.CharField('Название кафедры', max_length=150)
    email = models.CharField('Почта', max_length=50)
    phone_number = models.CharField('Номер телефона', max_length=50)
    address = models.CharField('Адрес', max_length=100)
    manager_department = models.OneToOneField(
        'profiles.Profile',
        related_name='manager_department',
        verbose_name="Заведущий кафедры",
        on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.TextField('Описание')
    timetable_department = models.FileField('Рассписание', upload_to='timetable-d/', null=True, blank=True)
    photo = models.ImageField('Фотография', upload_to='department/')
    photos = models.ImageField('Фотографии', upload_to='department/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"
