import uuid

from django.db import models

from merches.models import Ambassador


class Achieve(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    achieve_name = models.CharField(
        max_length=255, verbose_name='Название ачивки'
    )
    available = models.BooleanField(
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Ачивки'
        verbose_name_plural = 'Ачивки'

    def __str__(self):
        return self.achieve_name


class AmbassadorAchieve(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    achieve = models.ForeignKey(Achieve, on_delete=models.PROTECT)
    ambassador = models.ForeignKey(Ambassador, on_delete=models.PROTECT)
    assignment_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата получения ачивки'
    )

    class Meta:
        verbose_name = 'Ачивки амбассадоров'
        verbose_name_plural = 'Ачивки амбассадоров'

    def __str__(self):
        return f'{self.ambassador} - {self.achieve}'
