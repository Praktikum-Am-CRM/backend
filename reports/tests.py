# import datetime
# import os
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.test import TestCase
# from .models import Report, Placement, ReportStatus, ReportType
# from ambassador.models import Ambassador

# class ReportModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Создаем объекты, необходимые для тестов
#         ambassador = Ambassador.objects.create(
#             name='Test Ambassador', email='ambassador@example.com')
#         placement = Placement.objects.create(site='Test Site')
#         status = ReportStatus.objects.create(status_name='Test Status')
#         report_type = ReportType.objects.create(type_name='Test Type')

#         # Создаем объект отчета
#         cls.report = Report.objects.create(
#             ambassador=ambassador,
#             content_link='http://example.com/content',
#             placement=placement,
#             report_status=status,
#             sign_junior=False,
#             grade=5,
#             report_type=report_type
#         )

#         # Загружаем тестовый файл для поля 'screen'
#         cls.screen_path = os.path.join(
#             os.path.dirname(__file__), 'test_files', 'test_screen.png')
#         with open(cls.screen_path, 'rb') as file:
#             cls.screen_data = file.read()
#         cls.screen_file = SimpleUploadedFile(
#             'test_screen.png', cls.screen_data, content_type='image/png')

#     def test_report_str_representation(self):
#         """Тестирование строкового представления объекта Report."""
#         expected_str = (
#             f'{self.report.ambassador} - '
#             f'{self.report.placement} - {self.report.report_date}')
#         self.assertEqual(str(self.report), expected_str)

#     def test_report_defaults(self):
#         """Тестирование значений по умолчанию."""
#         report = Report.objects.create(
#             ambassador=Ambassador.objects.create(
#                 name='Test Default Ambassador', email='default@example.com'),
#             content_link='http://example.com/default',
#             placement=Placement.objects.create(site='Default Site'),
#             report_type=ReportType.objects.create(type_name='Default Type')
#         )
#         self.assertFalse(report.sign_junior)
#         self.assertEqual(report.grade, 1)

#     def test_report_screen_upload(self):
#         """Тестирование загрузки скриншота."""
#         self.report.screen = self.screen_file
#         self.report.save()
#         saved_report = Report.objects.get(id=self.report.id)
#         self.assertTrue(saved_report.screen.name.endswith('test_screen.png'))

#     def test_report_date_auto_now_add(self):
#         """Тестирование автоматического заполнения даты отчета."""
#         now = datetime.date.today()
#         report = Report.objects.create(
#             ambassador=Ambassador.objects.create(
#                 name='Test Date Ambassador', email='date@example.com'),
#             content_link='http://example.com/date',
#             placement=Placement.objects.create(site='Date Site'),
#             report_type=ReportType.objects.create(type_name='Date Type')
#         )
#         self.assertEqual(report.report_date, now)
