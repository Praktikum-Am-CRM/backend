import uuid

from django.db import models


class Ambassador(models.Model):
    pass


class TelegramBot(models.Model):
    '''Данные амбассадора из Telegram.'''
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    id_ambassador = models.OneToOneField(
        to=Ambassador,
        on_delete=models.PROTECT,
        related_name='telegram_bot'
    )
    nickname = models.CharField(
        max_length=100,
        verbose_name='Telegram Username'
    )
    active = models.BooleanField(default=False)
    registration_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата запуска бота пользователем'
    )

    def __str__(self):
        return f"Telegram инфо амбассадора с никнеймом {self.nickname}"
