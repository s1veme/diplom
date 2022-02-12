from django.db import models
from datetime import date
from django.urls import reverse
import departments.models
from shortuuid.django_fields import ShortUUIDField
import uuid

class Speciality(models.Model):
    """Специальности"""
    id = ShortUUIDField(
        primary_key=True, length=10, unique=True, default=uuid.uuid4().hex[:10], editable=False
    )
    name = models.CharField("имя специальность", max_length=150)
    department = models.ForeignKey('departments.Department', verbose_name="Кафедра", on_delete=models.CASCADE,
                                   blank=True, null=True)
    education_time = models.CharField('Время обучения', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"
