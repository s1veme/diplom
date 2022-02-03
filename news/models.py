from django.db import models
from datetime import date
from django.urls import reverse
import departments.models


class News(models.Model):
    """Новости"""
    name = models.CharField("Имя новости", max_length=150)
    description = models.TextField("Описание")
    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE)
    photo = models.ImageField('Фотография', upload_to='department/', blank=True)
    photos = models.ImageField('Фотографии', upload_to='department/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"