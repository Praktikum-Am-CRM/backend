from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("achievements", "0001_initial"),
        ("program", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Activity",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "activity_name",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        verbose_name="Вид деятельности",
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
                "verbose_name": "Вид деятельности",
                "verbose_name_plural": "Виды деятельности",
            },
        ),
        migrations.CreateModel(
            name="Ambassador",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "promocode",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Промокод",
                    ),
                ),
                (
                    "receipt_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        verbose_name="Дата принятия в амбассадоры",
                    ),
                ),
                (
                    "reminder_counter",
                    models.PositiveIntegerField(
                        blank=True,
                        default=0,
                        verbose_name="Счетчик напоминалок",
                    ),
                ),
                (
                    "address_index",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Индекс",
                    ),
                ),
                (
                    "address_country",
                    models.CharField(max_length=50, verbose_name="Страна"),
                ),
                (
                    "address_region",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Регион",
                    ),
                ),
                (
                    "address_district",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Район",
                    ),
                ),
                (
                    "address_settlement",
                    models.CharField(
                        max_length=50, verbose_name="Населённый пункт"
                    ),
                ),
                (
                    "address_street",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Улица",
                    ),
                ),
                (
                    "address_house",
                    models.PositiveIntegerField(default=0, verbose_name="Дом"),
                ),
                (
                    "address_building",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Корпус",
                    ),
                ),
                (
                    "address_apartment",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Квартира",
                    ),
                ),
                (
                    "size_clothing",
                    models.CharField(
                        blank=True,
                        max_length=2,
                        null=True,
                        verbose_name="Размер одежды",
                    ),
                ),
                (
                    "size_choe",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Размер обуви"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=20,
                        null=True,
                        verbose_name="Телефон",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, verbose_name="Электронная почта"
                    ),
                ),
                (
                    "note",
                    models.TextField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Заметка",
                    ),
                ),
                ("blog_link", models.URLField(verbose_name="Ссылка на блог")),
                (
                    "place_work",
                    models.CharField(
                        max_length=200, verbose_name="Место работы"
                    ),
                ),
                (
                    "specialty_work",
                    models.CharField(max_length=100, verbose_name="Должность"),
                ),
                (
                    "educational_institution",
                    models.CharField(
                        max_length=200, verbose_name="Учебное заведение"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=50, verbose_name="Имя"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Фамилия"),
                ),
                (
                    "middle_name",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Отчество",
                    ),
                ),
                (
                    "gender",
                    models.CharField(max_length=50, verbose_name="Пол"),
                ),
                ("birthday", models.DateField(verbose_name="Дата рождения")),
            ],
            options={
                "verbose_name": "Амбасадор",
                "verbose_name_plural": "Амбасадоры",
            },
        ),
        migrations.CreateModel(
            name="AmbassadorStatus",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "status_name",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        verbose_name="Статус амбассадора",
                    ),
                ),
                (
                    "sort_level",
                    models.IntegerField(verbose_name="Уровень сортировки"),
                ),
                (
                    "available",
                    models.BooleanField(
                        default=True, verbose_name="Доступность"
                    ),
                ),
            ],
            options={
                "verbose_name": "Статус амбассадора",
                "verbose_name_plural": "Статусы амбассадора",
            },
        ),
        migrations.CreateModel(
            name="Goal",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "goal_name",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        verbose_name="Название цели",
                    ),
                ),
                ("available", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Цель обучения",
                "verbose_name_plural": "Цели обучения",
            },
        ),
        migrations.CreateModel(
            name="AmbassadorStatusHistory",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "assignment_date",
                    models.DateField(verbose_name="Дата присвоения"),
                ),
                (
                    "ambassador",
                    models.ForeignKey(
                        max_length=50,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="status_history",
                        to="ambassador.ambassador",
                        verbose_name="Амбассадор",
                    ),
                ),
                (
                    "ambassador_status",
                    models.ForeignKey(
                        max_length=50,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="status_history",
                        to="ambassador.ambassadorstatus",
                        verbose_name="Статус",
                    ),
                ),
            ],
            options={
                "verbose_name": "История присвоения статусов",
                "verbose_name_plural": "История присвоения статусов",
            },
        ),
        migrations.CreateModel(
            name="AmbassadorProgram",
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
                    "ambassador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="ambassador.ambassador",
                    ),
                ),
                (
                    "program",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="ambassadors",
                        to="program.program",
                    ),
                ),
            ],
            options={
                "verbose_name": "Программа амбассадоров",
                "verbose_name_plural": "Программы амбассадоров",
            },
        ),
        migrations.CreateModel(
            name="AmbassadorGoal",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "own_version",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Своя версия",
                    ),
                ),
                (
                    "ambassador",
                    models.ForeignKey(
                        max_length=50,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ambassador.ambassador",
                        verbose_name="Амбассадор",
                    ),
                ),
                (
                    "goal",
                    models.ForeignKey(
                        max_length=50,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ambassador.goal",
                        verbose_name="Цель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Цель обучения амбассадора",
                "verbose_name_plural": "Цели обучения амбассадора",
            },
        ),
        migrations.CreateModel(
            name="AmbassadorActivity",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "activity",
                    models.ForeignKey(
                        max_length=50,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ambassador.activity",
                        verbose_name="Вид деятельности",
                    ),
                ),
                (
                    "ambassador",
                    models.ForeignKey(
                        max_length=50,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ambassador.ambassador",
                        verbose_name="Амбассадор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вид деятельности амбассадора",
                "verbose_name_plural": "Виды деятельности амбассадора",
            },
        ),
        migrations.CreateModel(
            name="AmbassadorAchieve",
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
                    models.DateField(verbose_name="Дата получения ачивки"),
                ),
                (
                    "achieve",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="achievements.achieve",
                    ),
                ),
                (
                    "ambassador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="ambassador.ambassador",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ачивки амбассадоров",
                "verbose_name_plural": "Ачивки амбассадоров",
            },
        ),
        migrations.AddField(
            model_name="ambassador",
            name="achieves",
            field=models.ManyToManyField(
                blank=True,
                related_name="achieves",
                through="ambassador.AmbassadorAchieve",
                to="achievements.achieve",
            ),
        ),
        migrations.AddField(
            model_name="ambassador",
            name="activity",
            field=models.ManyToManyField(
                blank=True,
                related_name="goals",
                through="ambassador.AmbassadorActivity",
                to="ambassador.activity",
            ),
        ),
        migrations.AddField(
            model_name="ambassador",
            name="goals",
            field=models.ManyToManyField(
                related_name="goals",
                through="ambassador.AmbassadorGoal",
                to="ambassador.goal",
            ),
        ),
    ]
