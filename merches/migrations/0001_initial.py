from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AmbassadorRequest",
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
                    "assignment_date",
                    models.DateField(verbose_name="Дата создания запроса"),
                ),
            ],
            options={
                "verbose_name": "Заявки амбассадоров на мерч",
                "verbose_name_plural": "Заявки амбассадоров на мерч",
            },
        ),
        migrations.CreateModel(
            name="DeliveryAddress",
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
                    "is_confirmed",
                    models.BooleanField(
                        default=False, verbose_name="Адрес подтвержден?"
                    ),
                ),
                (
                    "index",
                    models.CharField(
                        help_text="Укажите шестизначный почтовый индекс.",
                        max_length=255,
                        verbose_name="Почтовый индекс",
                    ),
                ),
                (
                    "region",
                    models.CharField(
                        blank=True,
                        help_text="Введите название области или края.",
                        max_length=255,
                        verbose_name="Область",
                    ),
                ),
                (
                    "district",
                    models.CharField(
                        blank=True,
                        help_text="Заполните название района, округа или города.",
                        max_length=255,
                        verbose_name="Район",
                    ),
                ),
                (
                    "settlement",
                    models.CharField(
                        help_text="Укажите название поселка, села, деревни или города",
                        max_length=255,
                        verbose_name="Населенный пункт",
                    ),
                ),
                (
                    "street",
                    models.CharField(
                        blank=True,
                        help_text="Введите название улицы или проспекта.",
                        max_length=255,
                        verbose_name="Улица",
                    ),
                ),
                (
                    "house",
                    models.CharField(
                        help_text="Заполните номер дома.",
                        max_length=255,
                        verbose_name="Дом",
                    ),
                ),
                (
                    "building",
                    models.CharField(
                        blank=True,
                        help_text="Укажите номер корпуса (если есть).",
                        max_length=255,
                        verbose_name="Корпус",
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        help_text="Укажите страну",
                        max_length=255,
                        verbose_name="Страна",
                    ),
                ),
                (
                    "apartment",
                    models.CharField(
                        blank=True,
                        help_text="Заполните номер квартиры (если есть).",
                        max_length=255,
                        verbose_name="Квартира",
                    ),
                ),
            ],
            options={
                "verbose_name": "Адрес доставки",
                "verbose_name_plural": "Адрес доставки",
            },
        ),
        migrations.CreateModel(
            name="DeliveryHistory",
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
                    "assignment_date",
                    models.DateField(verbose_name="Дата присвоения"),
                ),
            ],
            options={
                "verbose_name": "История доставок",
                "verbose_name_plural": "История доставок",
            },
        ),
        migrations.CreateModel(
            name="DeliveryStatus",
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
                        verbose_name="Статус доставки",
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
                "verbose_name": "Статус доставки",
                "verbose_name_plural": "Статусы доставки",
            },
        ),
        migrations.CreateModel(
            name="Merch",
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
                    "merch_name",
                    models.CharField(
                        max_length=255,
                        unique=True,
                        verbose_name="Название мерча",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        verbose_name="Цена",
                    ),
                ),
                (
                    "intangible",
                    models.BooleanField(
                        default=False,
                        verbose_name="Признак нематериального мерча",
                    ),
                ),
                (
                    "available",
                    models.BooleanField(
                        default=True, verbose_name="Доступен мерч"
                    ),
                ),
            ],
            options={
                "verbose_name": "Мерч",
                "verbose_name_plural": "Мерч",
            },
        ),
        migrations.CreateModel(
            name="MerchRequest",
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
                    "delivery_address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="merch_requests",
                        to="merches.deliveryaddress",
                        verbose_name="Адрес доставки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заявки на мерчи",
                "verbose_name_plural": "Заявки на мерч",
            },
        ),
    ]
