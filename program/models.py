import uuid

from django.db import models

from backend.constants import MAX_NAME_LENGTH


class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    program_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        verbose_name='Название программы обучения',
        unique=True,
    )
    available = models.BooleanField(default=True, verbose_name='Доступна')

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'

    def __str__(self):
        return self.program_name
