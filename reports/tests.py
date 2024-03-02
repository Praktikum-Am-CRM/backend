import shutil
import tempfile

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.utils import timezone

from ambassador.models import Ambassador, AmbassadorStatus
from telegram.models import TelegramBot

from .models import Placement, Report, ReportStatus, ReportType

User = get_user_model()
TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class ReportModelTest(TestCase):
    """Тесты модели Report."""

    @classmethod
    def setUpTestData(cls):
        """Установка начальных данных для тестирования."""
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
        placement = Placement.objects.create(site='Test Site')
        status = ReportStatus.objects.create(status_name='Test Status')
        report_type = ReportType.objects.create(type_name='Test Type')

        cls.screen_data = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00'
            b'\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00'
            b'\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        cls.screen_file = SimpleUploadedFile(
            'test_screen.png', cls.screen_data, content_type='image/png'
        )
        cls.report = Report.objects.create(
            ambassador=cls.ambassador,
            content_link='http://example.com/content',
            placement=placement,
            report_status=status,
            sign_junior=False,
            grade=5,
            report_type=report_type,
            screen=cls.screen_file,
        )

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(TEMP_MEDIA_ROOT)

    def test_report_str_representation(self):
        """Тестирование строкового представления объекта Report."""
        expected_str = (
            f'{self.report.ambassador} - '
            f'{self.report.placement_id} - {self.report.report_date}'
        )
        self.assertEqual(str(self.report), expected_str)

    def test_report_screen_upload(self):
        """Тестирование загрузки скриншота."""
        saved_report = Report.objects.get(id=self.report.id)
        with saved_report.screen.open() as userpic_file:
            userpic_content = userpic_file.read()
        self.assertEqual(
            userpic_content, self.screen_data, 'Неверная картинка'
        )
