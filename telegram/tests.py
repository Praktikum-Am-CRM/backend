import uuid

from django.test import TestCase
from django.utils import timezone

from .models import TelegramBot


class TelegramBotModelTest(TestCase):
    def setUp(self):
        self.telegram_bot = TelegramBot.objects.create(
            telegram_id='123456789',
            nickname='test_user',
            registration_date=timezone.now(),
            active=True,
        )

    def test_telegram_bot_creation(self):
        """Тестирование создания модели TelegramBot."""
        self.assertTrue(isinstance(self.telegram_bot, TelegramBot))
        self.assertEqual(
            self.telegram_bot.__str__(),
            'Telegram инфо амбассадора с никнеймом '
            f'{self.telegram_bot.nickname}',
        )

    def test_telegram_bot_fields(self):
        """Тестирование полей модели TelegramBot."""
        self.assertEqual(self.telegram_bot.telegram_id, '123456789')
        self.assertEqual(self.telegram_bot.nickname, 'test_user')
        self.assertTrue(
            isinstance(self.telegram_bot.registration_date, timezone.datetime)
        )
        self.assertTrue(self.telegram_bot.active)

    def test_telegram_bot_uuid_field(self):
        """Тестирование поля UUID модели TelegramBot."""
        self.assertTrue(isinstance(self.telegram_bot.id, uuid.UUID))
        self.assertIsNotNone(self.telegram_bot.id)

    def test_telegram_bot_default_active(self):
        """Тестирование значения по умолчанию для поля 'active'."""
        new_bot = TelegramBot.objects.create(
            telegram_id='987654321',
            nickname='another_user',
            registration_date=timezone.now(),
        )
        self.assertTrue(new_bot.active)

    def test_telegram_bot_str_representation(self):
        """Тестирование строкового представления объекта TelegramBot."""
        self.assertEqual(
            str(self.telegram_bot),
            'Telegram инфо амбассадора с никнеймом '
            f'{self.telegram_bot.nickname}',
        )

    def test_telegram_bot_inactive(self):
        """Тестирование установки статуса 'inactive' для TelegramBot."""
        self.telegram_bot.active = False
        self.telegram_bot.save()
        self.assertFalse(
            TelegramBot.objects.get(id=self.telegram_bot.id).active
        )
