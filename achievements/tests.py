from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from ambassador.models import Ambassador, AmbassadorStatus
from telegram.models import TelegramBot

from .models import Achieve, AmbassadorAchieve

User = get_user_model()


class AchieveModelTest(TestCase):
    """Набор тестов для модели Achieve."""

    @classmethod
    def setUpTestData(cls):
        """Настройка начальных данных для тестирования модели Achieve."""
        cls.achieve = Achieve.objects.create(
            achieve_name='Test Achieve', available=True
        )

    def test_achieve_name_label(self):
        """Проверка метки поля 'achieve_name'."""
        field_label = self.achieve._meta.get_field('achieve_name').verbose_name
        self.assertEqual(field_label, 'Название ачивки')

    def test_achieve_unique_constraint(self):
        """Проверка уникальности поля 'achieve_name'."""
        with self.assertRaises(Exception):
            Achieve.objects.create(achieve_name='Test Achieve', available=True)

    def test_achieve_str_representation(self):
        """Проверка строкового представления объекта Achieve."""
        self.assertEqual(str(self.achieve), 'Test Achieve')


class AmbassadorAchieveModelTest(TestCase):
    """Набор тестов для модели AmbassadorAchieve."""

    @classmethod
    def setUpTestData(cls):
        """Настройка начальных данных для теста модели AmbassadorAchieve."""
        cls.telegram_bot = TelegramBot.objects.create(
            telegram_id='123456789',
            nickname='test_user',
            registration_date=timezone.now(),
            active=True,
        )
        cls.test_manager = User.objects.create_user(
            username="ElonMusk",
            email="elonmusk@example.com",
            first_name="Elon",
            last_name="Musk",
            middle_name="Reeve",
            profession="Entrepreneur",
        )
        cls.test_status = AmbassadorStatus.objects.create(
            status_name='Test Status', sort_level=1, available=True
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
        cls.achieve = Achieve.objects.create(
            achieve_name='Test Achieve', available=True
        )
        cls.assignment = AmbassadorAchieve.objects.create(
            achieve=cls.achieve,
            ambassador=cls.ambassador,
            assignment_date='2024-03-02',
        )

    def test_assignment_date_label(self):
        """Проверка метки поля 'assignment_date'."""
        field_label = self.assignment._meta.get_field(
            'assignment_date'
        ).verbose_name
        self.assertEqual(field_label, 'Дата получения ачивки')

    def test_ambassador_achieve_str_representation(self):
        """Проверка строкового представления объекта AmbassadorAchieve."""
        expected_str = (
            f'{self.assignment.ambassador} - '
            f'{self.assignment.achieve} - '
            f'{self.assignment.assignment_date}'
        )
        self.assertEqual(str(self.assignment), expected_str)
