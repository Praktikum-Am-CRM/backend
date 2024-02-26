import uuid

from django.db import models

from .validators import validate_one_to_ten

# from ambassadors.models import Ambassador


class Ambassador(models.Model):
    '''
    Амбассадор, заглушку можно будет удалить когда будет что импортировать.
    '''
    pass


class ReportStatus(models.Model):
    '''Статус отчета.'''
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    report_status = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.report_status


class ReportType(models.Model):
    '''Вид задания.'''
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    report_type = models.CharField(
        max_length=100,
        verbose_name='Вид задания'
    )
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.report_type


class Placement(models.Model):
    '''Площадка размещения задания.'''
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    site = models.CharField(
        max_length=100,
        verbose_name='Площадка размещения контента'
    )
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.site


class Report(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name='ID Отчета',
        unique=True
    )
    ambassador_id = models.ForeignKey(
        to=Ambassador,
        on_delete=models.PROTECT
    )
    report_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата отчета'
    )
    content_link = models.URLField(
        verbose_name='Ссылка на контент',
        help_text='Добавьте ссылку на контент',
        unique=True,
        null=False
    )
    screen = models.FileField(
        upload_to='media/reports/screens/',
        null=True,
        default=None
    )
    placement_id = models.ForeignKey(
        to=Placement,
        on_delete=models.PROTECT
    )
    report_status_id = models.ForeignKey(
        to=ReportStatus,
        on_delete=models.PROTECT
    )
    sign_junior = models.BooleanField()
    grade = models.PositiveSmallIntegerField(
        validators=[validate_one_to_ten]
    )
    report_type_id = models.ForeignKey(
        to=ReportType,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f'''
        Отчёт {self.id}
        о задании амбассадора {self.ambassador_id}
        на платформе {self.placement_id}
        создан {self.report_date}
        '''
