import uuid

from django.db import models

from ambassador.models import Ambassador

from .validators import validate_one_to_ten


class ReportStatus(models.Model):
    """Статус отчета."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status_name = models.CharField(
        max_length=100, unique=True, verbose_name='Статус отчета'
    )
    available = models.BooleanField(default=True, verbose_name='Доступность')

    class Meta:
        verbose_name = 'Статус отчета'
        verbose_name_plural = 'Статусы отчетов'

    def __str__(self):
        return self.status_name


class ReportType(models.Model):
    """Вид задания."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_name = models.CharField(
        max_length=100, verbose_name='Вид задания', unique=True
    )
    available = models.BooleanField(default=True, verbose_name='Доступность')

    class Meta:
        verbose_name = 'Тип задания'
        verbose_name_plural = 'Типы заданий'

    def __str__(self):
        return self.type_name


class Placement(models.Model):
    """Площадка размещения задания."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site = models.CharField(
        max_length=100,
        verbose_name='Площадка размещения контента',
        unique=True,
    )
    available = models.BooleanField(default=True, verbose_name='Доступность')

    class Meta:
        verbose_name = 'Площадка размещения отчета'
        verbose_name_plural = 'Площадки размещения отчетов'

    def __str__(self):
        return self.site


class Report(models.Model):
    """Отчет о выполнении задания."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name='ID Отчета',
        unique=True,
    )
    ambassador = models.ForeignKey(to=Ambassador, on_delete=models.PROTECT)
    report_date = models.DateField(verbose_name='Дата отчета')
    content_link = models.URLField(
        verbose_name='Ссылка на контент',
        help_text='Добавьте ссылку на контент',
        null=False,
    )
    screen = models.FileField(
        upload_to='reports/',
        null=True,
        default=None,
        verbose_name='Скриншот',
        blank=True,
    )
    placement = models.ForeignKey(to=Placement, on_delete=models.PROTECT)
    report_status = models.ForeignKey(
        to=ReportStatus,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    sign_junior = models.BooleanField(
        default=False, verbose_name='Начинающий амбассадор?'
    )
    grade = models.PositiveSmallIntegerField(
        validators=[validate_one_to_ten], default=1
    )
    report_type = models.ForeignKey(to=ReportType, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Отчет о задании'
        verbose_name_plural = 'Отчеты о заданиях'

    def __str__(self):
        return f'{self.ambassador} - {self.placement_id} - {self.report_date}'
