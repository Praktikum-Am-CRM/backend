from django.test import TestCase
from django.utils import timezone

from .models import TelegramBot


class TelegramBotModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем объект для тестирования
        cls.telegram_bot = TelegramBot.objects.create(
            telegram_id='123456789',
            nickname='test_user',
            registration_date=timezone.now(),
            active=True,
        )

    def test_telegram_bot_creation(self):
        """Тестирование создания объекта TelegramBot."""
        self.assertTrue(isinstance(self.telegram_bot, TelegramBot))
        self.assertEqual(self.telegram_bot.telegram_id, '123456789')
        self.assertEqual(self.telegram_bot.nickname, 'test_user')
        self.assertTrue(self.telegram_bot.registration_date)
        self.assertTrue(self.telegram_bot.active)

    def test_telegram_bot_str_representation(self):
        """Тестирование строкового представления объекта TelegramBot."""
        expected_str = 'test_user (123456789)'
        self.assertEqual(str(self.telegram_bot), expected_str)

    def test_telegram_bot_defaults(self):
        """Тестирование значений по умолчанию."""
        new_bot = TelegramBot.objects.create(
            telegram_id='987654321',
            nickname='another_user',
        )
        self.assertTrue(new_bot.active)
        self.assertTrue(new_bot.registration_date)
