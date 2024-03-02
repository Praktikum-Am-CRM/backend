from datetime import date, datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from telegram.models import TelegramBot

from .models import (
    Activity,
    Ambassador,
    AmbassadorActivity,
    AmbassadorGoal,
    AmbassadorStatus,
    AmbassadorStatusHistory,
    Goal,
)

User = get_user_model()


class AmbassadorModelTest(TestCase):
    """Набор тестов для модели Ambassador."""

    @classmethod
    def setUpTestData(cls):
        """Настройка начальных данных для тестирования модели Ambassador."""
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

    def test_ambassador_model_fields(self):
        """Проверяет поля модели Ambassador."""
        self.assertEqual(self.ambassador.promocode, 'TEST123')
        self.assertEqual(self.ambassador.manager.username, 'ElonMusk')
        self.assertEqual(self.ambassador.status.status_name, 'Test Status')
        self.assertEqual(
            datetime.strptime(
                str(self.ambassador.birthday), '%Y-%m-%d'
            ).date(),
            date(2000, 1, 1),
        )

    def test_ambassador_str_representation(self):
        """Проверяет строковое представление модели Ambassador."""
        expected_str = (
            f'{self.ambassador.first_name} ' f'{self.ambassador.last_name}'
        )
        self.assertEqual(str(self.ambassador), expected_str)


class AmbassadorGoalModelTest(AmbassadorModelTest):
    """Набор тестов для модели AmbassadorGoal."""

    def setUp(self):
        """Настройка начальных данных для теста модели AmbassadorGoal."""
        test_goal = Goal.objects.create(goal_name='Test Goal', available=True)
        AmbassadorGoal.objects.create(
            id=1, goal=test_goal, ambassador=self.ambassador
        )

    def test_ambassador_goal_str_representation(self):
        """Проверяет строковое представление модели AmbassadorGoal."""
        ambassador_goal = AmbassadorGoal.objects.get(id=1)
        expected_str = f'{ambassador_goal.ambassador} - {ambassador_goal.goal}'
        self.assertEqual(str(ambassador_goal), expected_str)


class AmbassadorActivityModelTest(AmbassadorModelTest):
    """Набор тестов для модели AmbassadorActivity."""

    def setUp(self):
        """Настройка начальных данных для теста модели AmbassadorActivity."""
        test_activity = Activity.objects.create(
            activity_name='Test Activity', available=True
        )
        AmbassadorActivity.objects.create(
            id=1, activity=test_activity, ambassador=self.ambassador
        )

    def test_ambassador_activity_str_representation(self):
        """Проверяет строковое представление модели AmbassadorActivity."""
        ambassador_activity = AmbassadorActivity.objects.get(id=1)
        expected_str = (
            f'{ambassador_activity.ambassador} - '
            f'{ambassador_activity.activity}'
        )
        self.assertEqual(str(ambassador_activity), expected_str)


class AmbassadorStatusHistoryModelTest(AmbassadorModelTest):
    """Набор тестов для модели AmbassadorStatusHistory."""

    def setUp(self):
        """Настройка данных для тестирования модели AmbassadorStatusHistory."""
        test_status = AmbassadorStatus.objects.create(
            status_name='Test Status 2', sort_level=1, available=True
        )
        AmbassadorStatusHistory.objects.create(
            id=1,
            ambassador=self.ambassador,
            ambassador_status=test_status,
            assignment_date=timezone.now(),
        )

    def test_ambassador_status_history_str_representation(self):
        """Проверяет строковое представление модели AmbassadorStatusHistory."""
        status_history = AmbassadorStatusHistory.objects.get(id=1)
        expected_str = (
            f'{status_history.ambassador} - '
            f'{status_history.ambassador_status} - '
            f'{status_history.assignment_date}'
        )
        self.assertEqual(str(status_history), expected_str)
