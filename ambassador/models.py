from django.core.validators import MinLengthValidator
from django.db import models


class Ambassador(models.Model):
    telegram_bot_id = models.ForeignKey(
        "Telegram_bot",
        verbose_name="Телеграмм бот",
        on_delete=models.PROTECT
    )
    status_id = models.ForeignKey(
        "Status",
        verbose_name="Статус",
        on_delete=models.PROTECT)
    manager_id = models.ForeignKey(
        "Manager",
        verbose_name="Менеджер",
        on_delete=models.PROTECT
    )
    promocode = models.CharField(
        verbose_name='Промокод',
    )
    receipt_date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата"
    )
    reminder_counter = models.IntegerField(
        verbose_name="Счетчик напоминалок"
    )
    adress_index = models.CharField(
        verbose_name="Индекс",
        blank=True
    )
    adress_country = models.CharField(
        verbose_name="Страна"
    )
    adress_region = models.CharField(
        verbose_name="Регион"
    )
    adress_district = models.CharField(
        verbose_name="Район",
        blank=True
    )
    adress_settlement = models.CharField(
        verbose_name="Населённый пункт"
    )
    adress_street = models.CharField(
        verbose_name="Улица",
        blank=True
    )
    adress_house = models.IntegerField(verbose_name="Дом")
    adress_building = models.CharField(
        verbose_name="Корпус",
        blank=True
    )
    adress_apartment = models.CharField(
        verbose_name="Квартира",
        blank=True
    )
    size_clothing = models.CharField(
        verbose_name="Размер одежды"
    )
    size_choe = models.IntegerField(
        verbose_name="Размер обуви"
    )
    phone = models.CharField(
        verbose_name="Телефон",
        max_length=18,
        validators=[
            MinLengthValidator(14, message='Минимум 14 символов'),
        ],
    )
    email = models.EmailField()
    note = models.TextField(
        verbose_name="Заметка",
        blank=True
    )
    blog_link = models.URLField(
        verbose_name="Ссылка на блог"
    )
    place_work = models.CharField(
        verbose_name="Место работы"
    )
    specialty_work = models.CharField(
        verbose_name="Должность"
    )
    educational_institution = models.CharField(
        verbose_name="Учебное заведение"
    )

    class Meta:
        verbose_name = 'Амбасадор'
        verbose_name_plural = 'Амбасадоры'


class AmbassadorGoal(models.Model):
    goal_id = models.ForeignKey(
        "Goal",
        verbose_name="Цель",
        on_delete=models.CASCADE
    )
    ambassador_id = models.ForeignKey(
        "Ambassador",
        verbose_name="Амбассадор",
        on_delete=models.CASCADE
    )


class Goal(models.Model):
    goal_name = models.CharField(
        verbose_name="Название цели"
    )


class AmbassadorActivity(models.Model):
    activity_id = models.ForeignKey(
        "Activity",
        verbose_name="Активный",
        on_delete=models.CASCADE
    )
    ambassador_id = models.ForeignKey(
        "Ambassador",
        verbose_name="Амбассадор",
        on_delete=models.CASCADE
    )


class Activity(models.Model):
    type_of_activity = models.CharField(
        verbose_name="Вид деятельности"
    )


class AmbassadorAchive(models.Model):
    achive_id = models.ForeignKey(
        "Achive",
        verbose_name="Достижения",
        on_delete=models.CASCADE
    )
    ambassador_id = models.ForeignKey(
        "Ambassador",
        verbose_name="Амбассадор",
        on_delete=models.CASCADE
    )
    assignment_date = models.DateField(
        verbose_name="Дата выполнения",
        auto_now_add=True
    )


class Achive(models.Model):
    achive_name = models.CharField(
        verbose_name="Достижение"
    )


class AmbassadorStatusHistory(models.Model):
    ambassador_id = models.ForeignKey(
        "Ambassador",
        verbose_name="Амбассадор",
        on_delete=models.CASCADE
    )
    ambassador_status_id = models.ForeignKey(
        "AmbassadorStatus",
        verbose_name="Статус",
        on_delete=models.PROTECT
    )
    assignment_date = models.DateField(
        verbose_name="Дата"
    )


class AmbassadorStatus(models.Model):
    report_status = models.CharField(
        verbose_name="Статус отчета"
    )
    sort_level = models.IntegerField()
    available = models.BooleanField()
