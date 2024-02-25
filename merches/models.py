import uuid

from django.db import models


class Ambassador(models.Model):
    pass


class Status(models.TextChoices):
    PENDING = "pending", "Ожидание подтверждения"
    CONFIRMED = "confirmed", "Подтвержден"
    CANCEL = "cancel", "Отклонен"


class RequestAmbassador(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ambassador = models.ForeignKey(Ambassador, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Заявки амбассадоров"
        verbose_name_plural = "Заявки амбассадоров"

    def __str__(self):
        return self.id


class Merch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    merchandise_name = models.CharField(
        max_length=255, verbose_name="Название мерча"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена"
    )
    intangible_attribute = models.BooleanField(
        verbose_name="Признак нематериального мерча"
    )

    class Meta:
        verbose_name = "Мерч"
        verbose_name_plural = "Мерч"

    def __str__(self):
        return self.merchandise_name


class DeliveryAddress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    index = models.CharField(max_length=255, verbose_name="Почтовый индекс")
    region = models.CharField(max_length=255, verbose_name="Область")
    area = models.CharField(max_length=255, verbose_name="Район")
    locality = models.CharField(
        max_length=255, verbose_name="Населенный пункт"
    )
    street = models.CharField(max_length=255, verbose_name="Улица")
    house = models.CharField(max_length=255, verbose_name="Дом")
    building = models.CharField(
        max_length=255, verbose_name="Корпус", blank=True
    )
    structure = models.CharField(
        max_length=255, verbose_name="Строение", blank=True
    )
    apartment = models.CharField(
        max_length=255, verbose_name="Квартира", blank=True
    )
    address_confirmation_status = models.CharField(
        max_length=255,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name="Статус подтверждения адреса",
    )

    index.help_text = "Укажите шестизначный почтовый индекс."
    region.help_text = "Введите название области или края."
    area.help_text = "Заполните название района, округа или города."
    locality.help_text = "Укажите название поселка, села, деревни или города."
    street.help_text = "Введите название улицы или проспекта."
    house.help_text = "Заполните номер дома."
    building.help_text = "Укажите номер корпуса (если есть)."
    structure.help_text = "Введите номер строения (если есть)."
    apartment.help_text = "Заполните номер квартиры (если есть)."

    class Meta:
        verbose_name = "Адрес доставки"
        verbose_name_plural = "Адрес доставки"

    def __str__(self):
        return str(self.id)


class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    request_date = models.DateTimeField(verbose_name="Дата отправки")
    date_transfer_to_logist = models.DateTimeField(
        null=True, blank=True, verbose_name="Дата передачи логистам"
    )
    request_status = models.CharField(
        max_length=255,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name="Статус выполнения",
    )
    merchandise = models.ForeignKey(Merch, on_delete=models.PROTECT)
    delivery_address = models.ForeignKey(
        DeliveryAddress, on_delete=models.PROTECT
    )
    ambassador = models.ForeignKey(RequestAmbassador, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Заявки на мерчи"
        verbose_name_plural = "Заявки на мерч"

    def __str__(self):
        return str(self.id)
