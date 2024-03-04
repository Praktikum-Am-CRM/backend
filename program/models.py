import uuid

from django.db import models

from ambassador.models import Ambassador


class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    program_name = models.CharField(
        max_length=50, verbose_name='Название программы обучения', unique=True
    )
    available = models.BooleanField(default=True, verbose_name='Доступна')

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'

    def __str__(self):
        return self.program_name


class AmbassadorProgram(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ambassador = models.ForeignKey(Ambassador, on_delete=models.PROTECT)
    program = models.ForeignKey(Program, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Программа амбассадоров'
        verbose_name_plural = 'Программы амбассадоров'

    def __str__(self):
        return f'{self.ambassador} - {self.program}'
