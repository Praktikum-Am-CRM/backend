import uuid

from django.db import models

from merches.models import Ambassador


class Achieve(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    achieve_name = models.CharField(
        max_length=255, verbose_name='Название ачивки'
    )

    class Meta:
        verbose_name = 'Ачивки'
        verbose_name_plural = 'Ачивки'

    def __str__(self):
        return self.achieve_name


class AchieveAmbassador(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_ambassador = models.ForeignKey(Ambassador, on_delete=models.PROTECT)
    id_achieve = models.ForeignKey(Achieve, on_delete=models.PROTECT)
    assignment_date_achieve = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата получения ачивки'
    )

    class Meta:
        verbose_name = 'Ачивки амбассадоров'
        verbose_name_plural = 'Ачивки амбассадоров'

    def __str__(self):
        return f'{self.id_ambassador} - {self.id_achieve}'
