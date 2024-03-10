import uuid

from django.db import models

from backend.constants import MAX_NAME_LENGTH


class Achieve(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    achieve_name = models.CharField(
        max_length=MAX_NAME_LENGTH, verbose_name='Название ачивки', unique=True
    )
    available = models.BooleanField(default=True, verbose_name='Доступна')

    class Meta:
        verbose_name = 'Ачивки'
        verbose_name_plural = 'Ачивки'

    def __str__(self):
        return self.achieve_name
