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
    telegram_id = models.CharField(
        max_length=100,
        verbose_name='Telegram chat ID'
    )
    nickname = models.CharField(
        max_length=100,
        verbose_name='Telegram Username'
    )
    registration_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата запуска бота пользователем'
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Telegram инфо амбассадора с никнеймом {self.nickname}"
