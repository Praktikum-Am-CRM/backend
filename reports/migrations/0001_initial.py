from django.db import migrations, models
import django.db.models.deletion
import reports.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ambassador", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Placement",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "site",
                    models.CharField(
                        max_length=100,
                        unique=True,
                        verbose_name="Площадка размещения контента",
                    ),
                ),
                (
                    "available",
                    models.BooleanField(
                        default=True, verbose_name="Доступность"
                    ),
                ),
            ],
            options={
                "verbose_name": "Площадка размещения отчета",
                "verbose_name_plural": "Площадки размещения отчетов",
            },
        ),
        migrations.CreateModel(
            name="ReportStatus",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "status_name",
                    models.CharField(
                        max_length=100,
                        unique=True,
                        verbose_name="Статус отчета",
                    ),
                ),
                (
                    "available",
                    models.BooleanField(
                        default=True, verbose_name="Доступность"
                    ),
                ),
            ],
            options={
                "verbose_name": "Статус отчета",
                "verbose_name_plural": "Статусы отчетов",
            },
        ),
        migrations.CreateModel(
            name="ReportType",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "type_name",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Вид задания"
                    ),
                ),
                (
                    "available",
                    models.BooleanField(
                        default=True, verbose_name="Доступность"
                    ),
                ),
            ],
            options={
                "verbose_name": "Тип задания",
                "verbose_name_plural": "Типы заданий",
            },
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="ID Отчета",
                    ),
                ),
                ("report_date", models.DateField(verbose_name="Дата отчета")),
                (
                    "content_link",
                    models.URLField(
                        help_text="Добавьте ссылку на контент",
                        verbose_name="Ссылка на контент",
                    ),
                ),
                (
                    "screen",
                    models.FileField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to="reports/",
                        verbose_name="Скриншот",
                    ),
                ),
                (
                    "sign_junior",
                    models.BooleanField(
                        default=False, verbose_name="Начинающий амбассадор?"
                    ),
                ),
                (
                    "grade",
                    models.PositiveSmallIntegerField(
                        default=1,
                        validators=[reports.validators.validate_zero_to_ten],
                    ),
                ),
                (
                    "ambassador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reports",
                        to="ambassador.ambassador",
                    ),
                ),
                (
                    "placement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reports",
                        to="reports.placement",
                    ),
                ),
                (
                    "report_status",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reports",
                        to="reports.reportstatus",
                    ),
                ),
                (
                    "report_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reports",
                        to="reports.reporttype",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отчет о задании",
                "verbose_name_plural": "Отчеты о заданиях",
            },
        ),
    ]
