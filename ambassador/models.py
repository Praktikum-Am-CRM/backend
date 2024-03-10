import uuid

from django.db import models

from achievements.models import Achieve
from backend.constants import MAX_NAME_LENGTH, MAX_STATUS_TYPE_NAME_LENGTH
from program.models import Program
from telegram.models import TelegramBot
from users.models import Manager


class Ambassador(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True
    )
    telegram_bot = models.ForeignKey(
        TelegramBot,
        verbose_name="Телеграмм бот",
        max_length=50,
        on_delete=models.PROTECT,
        related_name='ambassadors',
    )
    status = models.ForeignKey(
        "AmbassadorStatus",
        verbose_name="Статус",
        max_length=MAX_STATUS_TYPE_NAME_LENGTH,
        on_delete=models.PROTECT,
        related_name='ambassadors',
    )
    manager = models.ForeignKey(
        Manager,
        verbose_name="Менеджер",
        max_length=50,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='ambassadors',
    )
    promocode = models.CharField(
        verbose_name='Промокод',
        max_length=255,
        blank=True,
        null=True,
    )
    receipt_date = models.DateField(
        verbose_name="Дата принятия в " "амбассадоры", blank=True, null=True
    )
    reminder_counter = models.PositiveIntegerField(
        verbose_name="Счетчик напоминалок",
        blank=True,
        default=0,
    )
    address_index = models.CharField(
        verbose_name="Индекс",
        max_length=10,
        blank=True,
        null=True,
    )
    address_country = models.CharField(
        verbose_name="Страна",
        max_length=50,
        blank=False,
        null=False,
    )
    address_region = models.CharField(
        verbose_name="Регион",
        max_length=50,
        blank=True,
        null=True,
    )
    address_district = models.CharField(
        verbose_name="Район",
        max_length=50,
        blank=True,
        null=True,
    )
    address_settlement = models.CharField(
        verbose_name="Населённый пункт",
        max_length=50,
        blank=False,
        null=False,
    )
    address_street = models.CharField(
        verbose_name="Улица",
        max_length=50,
        blank=True,
        null=True,
    )
    address_house = models.PositiveIntegerField(verbose_name="Дом", default=0)
    address_building = models.CharField(
        verbose_name="Корпус",
        max_length=10,
        blank=True,
        null=True,
    )
    address_apartment = models.CharField(
        verbose_name="Квартира",
        max_length=10,
        blank=True,
        null=True,
    )
    size_clothing = models.CharField(
        verbose_name="Размер одежды",
        max_length=2,
        blank=True,
        null=True,
    )
    size_choe = models.PositiveIntegerField(
        verbose_name="Размер обуви", default=0
    )
    phone = models.CharField(
        verbose_name="Телефон",
        max_length=20,
        blank=True,
        null=True,
        default='',
    )
    email = models.EmailField(verbose_name='Электронная почта')
    note = models.TextField(
        verbose_name="Заметка",
        max_length=200,
        blank=True,
        null=True,
    )
    blog_link = models.URLField(verbose_name="Ссылка на блог")
    place_work = models.CharField(verbose_name="Место работы", max_length=200)
    specialty_work = models.CharField(verbose_name="Должность", max_length=100)
    educational_institution = models.CharField(
        verbose_name="Учебное заведение",
        max_length=200,
    )
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=50,
    )
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    middle_name = models.CharField(
        verbose_name="Отчество", max_length=50, blank=True, null=True
    )
    gender = models.CharField(verbose_name="Пол", max_length=50)
    birthday = models.DateField(verbose_name="Дата рождения")
    programs = models.ManyToManyField(
        Program,
        blank=False,
        related_name='programs',
        through='AmbassadorProgram',
    )
    goals = models.ManyToManyField(
        'Goal',
        blank=False,
        related_name='goals',
        through='AmbassadorGoal',
    )
    activity = models.ManyToManyField(
        'Activity',
        blank=True,
        related_name='goals',
        through='AmbassadorActivity',
    )
    achieves = models.ManyToManyField(
        Achieve,
        blank=True,
        related_name='achieves',
        through='AmbassadorAchieve',
    )

    class Meta:
        verbose_name = 'Амбасадор'
        verbose_name_plural = 'Амбасадоры'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class AmbassadorGoal(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True
    )
    goal = models.ForeignKey(
        "Goal",
        verbose_name="Цель",
        max_length=MAX_NAME_LENGTH,
        on_delete=models.CASCADE,
    )
    ambassador = models.ForeignKey(
        "Ambassador",
        verbose_name="Амбассадор",
        max_length=50,
        on_delete=models.CASCADE,
    )
    own_version = models.CharField(
        verbose_name='Своя версия',
        max_length=250,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Цель обучения амбассадора'
        verbose_name_plural = 'Цели обучения амбассадора'

    def __str__(self):
        return f'{self.ambassador} - {self.goal}'


class Goal(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    goal_name = models.CharField(
        verbose_name="Название цели", max_length=MAX_NAME_LENGTH, unique=True
    )
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Цель обучения'
        verbose_name_plural = 'Цели обучения'

    def __str__(self):
        return f'{self.goal_name}'


class AmbassadorActivity(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True
    )
    activity = models.ForeignKey(
        "Activity",
        verbose_name="Вид деятельности",
        max_length=MAX_NAME_LENGTH,
        on_delete=models.CASCADE,
    )
    ambassador = models.ForeignKey(
        "Ambassador",
        verbose_name="Амбассадор",
        max_length=50,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Вид деятельности амбассадора'
        verbose_name_plural = 'Виды деятельности амбассадора'

    def __str__(self):
        return f'{self.ambassador} - {self.activity}'


class Activity(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    activity_name = models.CharField(
        verbose_name="Вид деятельности",
        max_length=MAX_NAME_LENGTH,
        unique=True,
    )
    available = models.BooleanField(default=True, verbose_name='Доступность')

    class Meta:
        verbose_name = 'Вид деятельности'
        verbose_name_plural = 'Виды деятельности'

    def __str__(self):
        return f'{self.activity_name}'


class AmbassadorStatusHistory(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    ambassador = models.ForeignKey(
        "Ambassador",
        verbose_name="Амбассадор",
        max_length=50,
        on_delete=models.CASCADE,
        related_name='status_history',
    )
    ambassador_status = models.ForeignKey(
        "AmbassadorStatus",
        verbose_name="Статус",
        max_length=MAX_NAME_LENGTH,
        on_delete=models.PROTECT,
        related_name='status_history',
    )
    assignment_date = models.DateField(verbose_name='Дата присвоения')

    class Meta:
        verbose_name = 'История присвоения статусов'
        verbose_name_plural = 'История присвоения статусов'

    def __str__(self):
        return (
            f'{self.ambassador} - '
            f'{self.ambassador_status} - '
            f'{self.assignment_date}'
        )


class AmbassadorStatus(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    status_name = models.CharField(
        verbose_name="Статус амбассадора",
        max_length=MAX_NAME_LENGTH,
        unique=True,
    )
    sort_level = models.IntegerField(verbose_name='Уровень сортировки')
    available = models.BooleanField(default=True, verbose_name='Доступность')

    class Meta:
        verbose_name = 'Статус амбассадора'
        verbose_name_plural = 'Статусы амбассадора'

    def __str__(self):
        return f'{self.status_name}'


class AmbassadorProgram(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ambassador = models.ForeignKey(Ambassador, on_delete=models.PROTECT)
    program = models.ForeignKey(
        Program, on_delete=models.PROTECT, related_name='ambassadors'
    )

    class Meta:
        verbose_name = 'Программа амбассадоров'
        verbose_name_plural = 'Программы амбассадоров'

    def __str__(self):
        return f'{self.ambassador} - {self.program}'


class AmbassadorAchieve(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    achieve = models.ForeignKey(Achieve, on_delete=models.PROTECT)
    ambassador = models.ForeignKey(Ambassador, on_delete=models.PROTECT)
    assignment_date = models.DateField(verbose_name='Дата получения ачивки')

    class Meta:
        verbose_name = 'Ачивки амбассадоров'
        verbose_name_plural = 'Ачивки амбассадоров'

    def __str__(self):
        return f'{self.ambassador} - {self.achieve} - {self.assignment_date}'
