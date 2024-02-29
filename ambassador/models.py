import uuid

from django.core.validators import MinLengthValidator
from django.db import models

from telegram.models import TelegramBot
from users.models import Manager


class Ambassador(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True
    )
    telegram_bot_id = models.ForeignKey(
        TelegramBot,
        verbose_name="Телеграмм бот",
        max_length=50,
        on_delete=models.PROTECT,
    )
    status_id = models.ForeignKey(
        "AmbassadorStatus",
        verbose_name="Статус",
        max_length=50,
        on_delete=models.PROTECT,
    )
    manager_id = models.ForeignKey(
        Manager,
        verbose_name="Менеджер",
        max_length=50,
        blank=True,
        on_delete=models.PROTECT,
    )
    promocode = models.CharField(
        verbose_name='Промокод', max_length=255, blank=True
    )
    receipt_date = models.DateField(
        auto_now_add=True, verbose_name="Дата", blank=True
    )
    reminder_counter = models.PositiveIntegerField(
        verbose_name="Счетчик напоминалок", blank=True
    )
    adress_index = models.CharField(verbose_name="Индекс", max_length=10)
    adress_country = models.CharField(verbose_name="Страна", max_length=50)
    adress_region = models.CharField(verbose_name="Регион", max_length=50)
    adress_district = models.CharField(
        verbose_name="Район", max_length=50, blank=True
    )
    adress_settlement = models.CharField(
        verbose_name="Населённый пункт", max_length=50
    )
    adress_street = models.CharField(
        verbose_name="Улица", max_length=50, blank=True
    )
    adress_house = models.PositiveIntegerField(verbose_name="Дом")
    adress_building = models.CharField(
        verbose_name="Корпус", max_length=10, blank=True
    )
    adress_apartment = models.CharField(
        verbose_name="Квартира", max_length=10, blank=True
    )
    size_clothing = models.CharField(
        verbose_name="Размер одежды",
        max_length=2,
    )
    size_choe = models.PositiveIntegerField(
        verbose_name="Размер обуви",
    )
    phone = models.CharField(
        verbose_name="Телефон",
        max_length=18,
        validators=[
            MinLengthValidator(14, message='Минимум 14 символов'),
        ],
    )
    email = models.EmailField()
    note = models.TextField(verbose_name="Заметка", max_length=50, blank=True)
    blog_link = models.URLField(verbose_name="Ссылка на блог")
    place_work = models.CharField(verbose_name="Место работы", max_length=50)
    specialty_work = models.CharField(verbose_name="Должность", max_length=50)
    educational_institution = models.CharField(
        verbose_name="Учебное заведение",
        max_length=50,
    )
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=50,
    )
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    middle_name = models.CharField(verbose_name="Отчество", max_length=50)
    gender = models.CharField(verbose_name="Пол", max_length=50)
    birthday = models.DateField(verbose_name="Дата рождения")

    class Meta:
        verbose_name = 'Амбасадор'
        verbose_name_plural = 'Амбасадоры'


class AmbassadorGoal(models.Model):
    goal_id = models.ForeignKey(
        "Goal", verbose_name="Цель", max_length=50, on_delete=models.CASCADE
    )
    ambassador_id = models.ForeignKey(
        "Ambassador",
        verbose_name="Амбассадор",
        max_length=50,
        on_delete=models.CASCADE,
    )


class Goal(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    goal_name = models.CharField(verbose_name="Название цели", max_length=50)
    available = models.BooleanField(default=True)


class AmbassadorActivity(models.Model):
    activity_id = models.ForeignKey(
        "Activity",
        verbose_name="Активный",
        max_length=50,
        on_delete=models.CASCADE,
    )
    ambassador_id = models.ForeignKey(
        "Ambassador",
        verbose_name="Амбассадор",
        max_length=50,
        on_delete=models.CASCADE,
    )


class Activity(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    activity_name = models.CharField(
        verbose_name="Вид деятельности", max_length=50
    )
    available = models.BooleanField(default=True)


class AmbassadorAchive(models.Model):
    achive_id = models.ForeignKey(
        "Achive",
        verbose_name="Достижения",
        max_length=50,
        on_delete=models.CASCADE,
    )
    ambassador_id = models.ForeignKey(
        "Ambassador",
        verbose_name="Амбассадор",
        max_length=50,
        on_delete=models.CASCADE,
    )
    assignment_date = models.DateField(
        verbose_name="Дата выполнения", auto_now_add=True
    )


# Есть ощущение что это заглушка пока не было отельного приложения и модели
class Achive(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    achive_name = models.CharField(
        verbose_name="Достижение",
        max_length=50,
    )
    available = models.BooleanField(default=True)


class AmbassadorStatusHistory(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    ambassador_id = models.ForeignKey(
        "Ambassador",
        verbose_name="Амбассадор",
        max_length=50,
        on_delete=models.CASCADE,
    )
    ambassador_status_id = models.ForeignKey(
        "AmbassadorStatus",
        verbose_name="Статус",
        max_length=50,
        on_delete=models.PROTECT,
    )
    assignment_date = models.DateField(verbose_name="Дата")


class AmbassadorStatus(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    # Статус отчета?
    status_name = models.CharField(verbose_name="Статус отчета", max_length=50)
    sort_level = models.IntegerField()
    available = models.BooleanField(default=True)
