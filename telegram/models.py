import uuid

from django.db import models

from backend.constants import MAX_NAME_LENGTH


class TelegramBot(models.Model):
    """Данные амбассадора из Telegram."""

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    telegram_id = models.CharField(
        max_length=100, verbose_name='Telegram chat ID'
    )
    nickname = models.CharField(
        max_length=MAX_NAME_LENGTH, verbose_name='Telegram Username'
    )
    registration_date = models.DateTimeField(
        verbose_name='Дата запуска бота пользователем'
    )
    active = models.BooleanField(default=True, verbose_name='Активный?')

    class Meta:
        verbose_name = 'Данные амбассадора в телеграм'
        verbose_name_plural = 'Данные амбассадора в телеграм'

    def __str__(self):
        return f'{self.nickname} ({self.telegram_id})'
