from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from ambassador.models import Ambassador, AmbassadorStatus
from telegram.models import TelegramBot
from users.models import Manager

from .models import (
    AmbassadorRequest,
    DeliveryAddress,
    DeliveryHistory,
    DeliveryStatus,
    Merch,
    MerchRequest,
)

User = get_user_model()


class ModelTests(TestCase):
    """Набор тестов для моделей."""

    @classmethod
    def setUpTestData(cls):
        """Настройка начальных данных для тестирования."""
        cls.manager = Manager.objects.create(
            username='manager1', email='manager1@example.com'
        )

        cls.delivery_address = DeliveryAddress.objects.create(
            id=1,
            is_confirmed=True,
            index='123456',
            region='Test Region',
            district='Test District',
            settlement='Test Settlement',
            street='Test Street',
            house='1',
            building='Test Building',
            country='Test Country',
            apartment='Test Apartment',
        )

        cls.delivery_status = DeliveryStatus.objects.create(
            id=1, status_name='In transit', available=True
        )

        cls.merch = Merch.objects.create(
            id=1, merch_name='Test Merch', price=10.50
        )

        cls.merch_request = MerchRequest.objects.create(
            id=1,
            manager=cls.manager,
            merch=cls.merch,
            delivery_address=cls.delivery_address,
            request_status=cls.delivery_status,
        )

        telegram_bot = TelegramBot.objects.create(
            telegram_id='123456789',
            nickname='test_user',
            registration_date=timezone.now(),
            active=True,
        )
        test_manager = User.objects.create_user(
            username='ElonMusk',
            email='elonmusk@example.com',
            first_name='Elon',
            last_name='Musk',
            middle_name='Reeve',
            profession='Entrepreneur',
        )
        test_status = AmbassadorStatus.objects.create(
            status_name='Test Status', sort_level=1, available=True
        )
        cls.ambassador = Ambassador.objects.create(
            telegram_bot=telegram_bot,
            status=test_status,
            manager=test_manager,
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

        cls.ambassador_request = AmbassadorRequest.objects.create(
            id=1,
            merch_request=cls.merch_request,
            ambassador=cls.ambassador,
            assignment_date=timezone.now(),
        )

        cls.delivery_history = DeliveryHistory.objects.create(
            id=1,
            merch_request=cls.merch_request,
            delivery_status=cls.delivery_status,
            assignment_date=timezone.now(),
        )

    def test_merch_name_label(self):
        """Проверяет метку поля 'merch_name' модели Merch."""
        merch = Merch.objects.get(id=1)
        field_label = merch._meta.get_field('merch_name').verbose_name
        self.assertEqual(field_label, 'Название мерча')

    def test_delivery_address_str_representation(self):
        """Проверяет строковое представление объекта DeliveryAddress."""
        delivery_address = DeliveryAddress.objects.get(id=1)
        expected_str = (
            f'{delivery_address.index} - {delivery_address.country} - '
            f'{delivery_address.region} - {delivery_address.district} - '
            f'{delivery_address.settlement} - {delivery_address.street} - '
            f'{delivery_address.house} - {delivery_address.building} - '
            f'{delivery_address.apartment}'
        )

        self.assertEqual(str(delivery_address), expected_str)

    def test_merch_request_str_representation(self):
        """Проверяет строковое представление объекта MerchRequest."""
        merch_request = MerchRequest.objects.get(id=1)
        expected_str = (
            f'{merch_request.merch} - ' f'{merch_request.request_status}'
        )
        self.assertEqual(str(merch_request), expected_str)

    def test_ambassador_request_assignment_date_label(self):
        """Проверяет метку поля 'assignment_date' модели AmbassadorRequest."""
        ambassador_request = AmbassadorRequest.objects.get(id=1)
        field_label = ambassador_request._meta.get_field(
            'assignment_date'
        ).verbose_name
        self.assertEqual(field_label, 'Дата создания запроса')

    def test_delivery_history_str_representation(self):
        """Проверяет строковое представление объекта DeliveryHistory."""
        delivery_history = DeliveryHistory.objects.get(id=1)
        expected_str = (
            f'{delivery_history.merch_request.merch} - '
            f'{delivery_history.delivery_status} - '
            f'{delivery_history.assignment_date}'
        )
        self.assertEqual(str(delivery_history), expected_str)
