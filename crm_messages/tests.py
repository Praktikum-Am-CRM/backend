from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from ambassador.models import Ambassador, AmbassadorStatus
from telegram.models import TelegramBot

from .models import (
    BotMessages,
    Message,
    MessagePool,
    MessageStatus,
    MessageType,
)

User = get_user_model()


class ModelTests(TestCase):
    """Набор тестов для моделей."""

    @classmethod
    def setUpTestData(cls):
        """Настройка начальных данных для тестирования."""
        cls.test_status = AmbassadorStatus.objects.create(
            status_name='Test Status', sort_level=1, available=True
        )
        cls.telegram_bot = TelegramBot.objects.create(
            telegram_id='123456789',
            nickname='test_user',
            registration_date=timezone.now(),
            active=True,
        )
        cls.test_manager = User.objects.create_user(
            username='ElonMusk',
            email='elonmusk@example.com',
            first_name='Elon',
            last_name='Musk',
            middle_name='Reeve',
            profession='Entrepreneur',
        )
        cls.ambassador = Ambassador.objects.create(
            telegram_bot=cls.telegram_bot,
            status=cls.test_status,
            manager=cls.test_manager,
            promocode='TEST123',
            receipt_date=timezone.now(),
            reminder_counter=0,
            address_index='123456',
            address_country='Test Country',
            address_region='Test Region',
            address_district='Test District',
            address_settlement='Test Settlement',
            address_street='Test Street',
            address_house=1,
            address_building='Test Building',
            address_apartment='Test Apartment',
            size_clothing='M',
            size_choe=42,
            phone='1234567890',
            email='test@example.com',
            note='Test Note',
            blog_link='http://example.com',
            place_work='Test Workplace',
            specialty_work='Test Specialty',
            educational_institution='Test Institution',
            first_name='Test',
            last_name='Ambassador',
            middle_name='Test',
            gender='Male',
            birthday='2000-01-01',
        )
        cls.message_type = MessageType.objects.create(
            type_name='Test Type', available=True
        )
        cls.message_status = MessageStatus.objects.create(
            status_name='Test Status', available=True
        )
        cls.message = Message.objects.create(
            message_text='Test message',
            date=timezone.now(),
            message_type=cls.message_type,
        )
        cls.bot_message = BotMessages.objects.create(
            message=cls.message,
            from_bot=True,
            manager=cls.test_manager,
            ambassador=cls.ambassador,
            sign_ai=True,
        )
        cls.message_pool = MessagePool.objects.create(
            message=cls.message,
            message_status=cls.message_status,
            send_date=datetime.now(),
        )

    def test_bot_message_str_representation(self):
        """Проверяет строковое представление объекта BotMessages."""
        self.assertEqual(
            str(self.bot_message), f'{self.ambassador} - {self.message}'
        )

    def test_message_type_str_representation(self):
        """Проверяет строковое представление объекта MessageType."""
        self.assertEqual(str(self.message_type), 'Test Type')

    def test_message_str_representation(self):
        """Проверяет строковое представление объекта Message."""
        self.assertEqual(str(self.message), 'Test message')

    def test_message_pool_str_representation(self):
        """Проверяет строковое представление объекта MessagePool."""
        self.assertEqual(
            str(self.message_pool),
            (
                f'{self.message_status} - '
                f'{self.message} - '
                f'{self.message_pool.send_date}'
            ),
        )
