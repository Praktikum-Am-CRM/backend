import uuid

from django.db import models

from .validators import validate_one_to_ten

# from ambassadors.models import Ambassador


class Ambassador(models.Model):
    '''
    Амбассадор, заглушку можно будет удалить когда будет что импортировать.
    '''
    pass


class RunStatus(models.Model):
    '''Статус отчета.'''
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    run_status = models.CharField(max_length=100)

    def __str__(self):
        return self.run_status


class TypeReport(models.Model):
    '''Вид задания.'''
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    type_report = models.CharField(
        max_length=100,
        verbose_name='Вид задания'
    )

    def __str__(self):
        return self.type_report


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
    id_ambassador = models.ForeignKey(
        to=Ambassador,
        on_delete=models.CASCADE
    )
    report_date = models.DateField(
        autonow=True,
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
    placement = models.ForeignKey(
        to=Placement,
        on_delete=models.CASCADE
    )
    sign_junior = models.BooleanField()
    id_run_status = models.ForeignKey(
        to=RunStatus,
        on_delete=models.CASCADE
    )
    grade = models.PositiveSmallIntegerField(
        validators=[validate_one_to_ten]
    )

    def __str__(self):
        return f'''
        Отчёт {self.id}
        о задании амбассадора {self.id_ambassador}
        на платформе {self.placement}
        создан {self.report_date}
        '''
