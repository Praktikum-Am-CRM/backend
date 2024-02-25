from django.core.validators import MinLengthValidator
from django.db import models


class Ambassador(models.Model):
    id = models.UUIDField(primary_key=True)
    form = models.ForeignKey("Forms", on_delete=models.CASCADE)
    telegram_bot = models.ForeignKey(
        "Telegram_bot",
        verbose_name="Телеграмм бот",
        on_delete=models.PROTECT
    )
    status = models.ForeignKey(
        "Status",
        verbose_name="Статус",
        on_delete=models.PROTECT)
    report = models.ForeignKey("Report", on_delete=models.PROTECT)
    messages = models.ForeignKey(
        "Messages",
        verbose_name="Сообщение",
        on_delete=models.PROTECT
    )
    manager = models.ForeignKey(
        "Manager",
        verbose_name="Менеджер",
        on_delete=models.PROTECT
    )
    promocode = models.CharField(
        max_length=10,
        verbose_name='Промокод',
        blank=True
    )
    date_receipt = models.DateField(
        auto_now_add=True,
        verbose_name="Дата"
    )
    reminder_counter = models.IntegerField(
        verbose_name="Счетчик напоминалок"
    )
    request = models.ForeignKey(
        "Request",
        verbose_name="Заявка на мерч",
        on_delete=models.PROTECT)
    achive = models.CharField(verbose_name="Ачивка")

    class Meta:
        verbose_name = 'Амбасадор'
        verbose_name_plural = 'Амбасадоры'


class Status(models.Model):
    STATUS = (
        ("0", "канидат"),
        ("1", "активный"),
        ("2", "на паузе"),
        ("3", "не амбасадор"),
        ("4", "уточняется"),
        ("5", "архив"),
    )

    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name="Статус")
    number = models.CharField(choices=STATUS, default="0")

    def __str__(self):
        return self.name


class Forms(models.Model):
    SEX_NAME = (
        ("муж", "мужчина"),
        ("жен", "женщина"),
    )

    id = models.UUIDField(primary_key=True)
    ambassador = models.ForeignKey(
        "Ambassador",
        verbose_name="Амбасадор",
        on_delete=models.CASCADE
    )
    last_name = models.TextField(verbose_name="Фамилия")
    first_name = models.TextField(verbose_name="Имя")
    middle_name = models.TextField(verbose_name="Отчество", blank=True)
    sex = models.CharField(choices=SEX_NAME, default="муж")
    birthday = models.DateField(
        verbose_name="Дата рождения",
        max_length=8
    )
    contact = models.ForeignKey(
        "Ambassador",
        verbose_name="Друг",
        on_delete=models.PROTECT
    )
    program = models.ForeignKey(
        "Program",
        verbose_name="Программа",
        on_delete=models.PROTECT
    )
    goal = models.ForeignKey(
        "Goal",
        verbose_name="Цель",
        on_delete=models.PROTECT
    )
    address = models.ForeignKey(
        "Address",
        verbose_name="Адрес",
        on_delete=models.PROTECT
    )
    size = models.ForeignKey(
        "Size",
        verbose_name="Размер",
        on_delete=models.PROTECT
    )
    activity = models.ForeignKey("Activity", on_delete=models.PROTECT)


class Adress(models.Model):
    id = models.UUIDField(primary_key=True)
    form = models.ForeignKey("Forms", on_delete=models.CASCADE)
    country = models.CharField(verbose_name="Страна")
    index = models.CharField(
        verbose_name="Индекс",
        blank=True
    )
    region = models.CharField(verbose_name="Регион")
    district = models.CharField(
        verbose_name="Район",
        blank=True
    )
    settlement = models.CharField(verbose_name="Населённый пункт")
    street = models.CharField(
        verbose_name="Улица",
        blank=True
    )
    house = models.IntegerField(verbose_name="Дом")
    building = models.CharField(verbose_name="Корпус", blank=True)
    apartment = models.CharField(verbose_name="Квартира", blank=True)


class Size(models.Model):
    form = models.ForeignKey("Forms", on_delete=models.CASCADE)
    clothing_size = models.CharField(verbose_name="Размер одежды")
    choe_size = models.CharField(verbose_name="Размер обуви")


class Program(models.Model):
    id = models.UUIDField(primary_key=True)
    program_name = models.CharField(
        verbose_name="Наименование программы"
    )


class Contact(models.Model):
    id = models.UUIDField(primary_key=True)
    form = models.ForeignKey("Forms", on_delete=models.CASCADE)
    phone = models.CharField(
        verbose_name="Телефон",
        max_length=18,
        validators=[
            MinLengthValidator(14, message='Минимум 14 символов'),
        ],
        blank=False
    )
    email = models.EmailField()


class Addendum(models.Model):
    id = models.UUIDField(primary_key=True)
    form = models.ForeignKey("Forms", on_delete=models.CASCADE)
    note = models.TextField(verbose_name="Заметка", blank=True)
    blog_link = models.URLField(verbose_name="Ссылка на блог")
    place_work = models.CharField(verbose_name="Место работы")
    specialty_work = models.CharField(verbose_name="Должность")
    educational_institution = models.CharField(
        verbose_name="Учебное заведение"
    )


class GoalAmmbassador(models.Model):
    id = models.ForeignKey("Goal", on_delete=models.CASCADE)
    form = models.ForeignKey("Forms", on_delete=models.CASCADE)
    goal_text = models.TextField(verbose_name="Текст цели")


class Goal(models.Model):
    id = models.UUIDField(primary_key=True)
    goal = models.CharField(verbose_name="Цель")


class ActivityAmbassador(models.Model):
    form = models.ForeignKey("Forms", on_delete=models.CASCADE)
    activity = models.ForeignKey("Activity", on_delete=models.CASCADE)


class Activity(models.Model):
    ACTIVITY_LIST = (
        ("1", "Вести блог"),
        ("2", "Развивать локальное профессиональное сообщество"
            "в своем городе"),
        ("3", "Писать статьи"),
        ("4", "Снимать видел или сниматься в них"
            "если продакшн будет на нашей стороне"),
        ("5", "Знакомить коллег на работе с продуктом Практикума"
            "через разлиные форматы"),
        ("6", "Давать консультации и рассказывать всем про Практикум"),
        ("7", "Выступать на мероприятиях"),
    )
    id = models.UUIDField(primary_key=True)
    type_of_activity = models.CharField(
        verbose_name="Вид деятельности",
        choices=ACTIVITY_LIST
    )


class StatusHistory(models.Model):
    id = models.UUIDField(primary_key=True)
    status = models.ForeignKey("Status", on_delete=models.CASCADE)
    ambassador = models.ForeignKey("Ambassador", on_delete=models.CASCADE)
    assignment_date_status = models.DateTimeField(
        verbose_name="Дата получения статуса",
        auto_now_add=True
    )
