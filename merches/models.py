import uuid

from django.db import models

from ambassador.models import Ambassador
from users.models import Manager


class Merch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    merch_name = models.CharField(
        max_length=255, verbose_name='Название мерча', unique=True
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена'
    )
    intangible = models.BooleanField(
        blank=True, null=True, verbose_name='Признак нематериального мерча'
    )
    available = models.BooleanField(default=True, verbose_name='Доступен мерч')

    class Meta:
        verbose_name = 'Мерч'
        verbose_name_plural = 'Мерч'

    def __str__(self):
        return self.merch_name


class DeliveryAddress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_confirmed = models.BooleanField(
        default=False, verbose_name='Адрес ' 'подтвержден?'
    )
    index = models.CharField(max_length=255, verbose_name='Почтовый индекс')
    region = models.CharField(max_length=255, verbose_name='Область')
    district = models.CharField(max_length=255, verbose_name='Район')
    settlement = models.CharField(
        max_length=255, verbose_name='Населенный пункт', blank=True
    )
    street = models.CharField(max_length=255, verbose_name='Улица')
    house = models.CharField(max_length=255, verbose_name='Дом')
    building = models.CharField(
        max_length=255, verbose_name='Корпус', blank=True
    )
    country = models.CharField(
        max_length=255, verbose_name='Страна', blank=True
    )
    apartment = models.CharField(
        max_length=255, verbose_name='Квартира', blank=True
    )

    index.help_text = 'Укажите шестизначный почтовый индекс.'
    region.help_text = 'Введите название области или края.'
    district.help_text = 'Заполните название района, округа или города.'
    settlement.help_text = 'Укажите название поселка, села, деревни или города'
    street.help_text = 'Введите название улицы или проспекта.'
    house.help_text = 'Заполните номер дома.'
    building.help_text = 'Укажите номер корпуса (если есть).'
    country.help_text = 'Укажите страну'
    apartment.help_text = 'Заполните номер квартиры (если есть).'

    class Meta:
        verbose_name = 'Адрес доставки'
        verbose_name_plural = 'Адрес доставки'

    def __str__(self):
        return (
            f'{self.index} - {self.country} - {self.region} - '
            f'{self.district} - '
            f'{self.settlement} - {self.street} - {self.house} - '
            f'{self.building} - {self.apartment}'
        )


class DeliveryStatus(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    delivery_status = models.CharField(
        max_length=100, unique=True, verbose_name='Статус доставки'
    )
    available = models.BooleanField(default=True, verbose_name='Доступность')

    class Meta:
        verbose_name = 'Статус доставки'
        verbose_name_plural = 'Статусы доставки'

    def __str__(self):
        return self.delivery_status


class MerchRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    manager = models.ForeignKey(
        Manager,
        on_delete=models.PROTECT,
        verbose_name='Менеджер',
    )
    merch = models.ForeignKey(
        Merch,
        on_delete=models.PROTECT,
        verbose_name='Мерч',
    )
    delivery_address = models.ForeignKey(
        DeliveryAddress,
        on_delete=models.PROTECT,
        verbose_name='Адрес доставки',
    )
    request_status = models.ForeignKey(
        DeliveryStatus,
        on_delete=models.PROTECT,
        verbose_name='Статус выполнения',
    )

    class Meta:
        verbose_name = 'Заявки на мерчи'
        verbose_name_plural = 'Заявки на мерч'

    def __str__(self):
        return f'{self.merch} - {self.request_status}'


class AmbassadorRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    merch_request = models.ForeignKey(
        MerchRequest,
        on_delete=models.PROTECT,
    )
    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.PROTECT,
    )
    assignment_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания запроса',
    )

    class Meta:
        verbose_name = 'Заявки амбассадоров на мерч'
        verbose_name_plural = 'Заявки амбассадоров на мерч'

    def __str__(self):
        return f'{self.ambassador} - {self.merch_request}'


class DeliveryHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    merch_request = models.ForeignKey(
        MerchRequest,
        on_delete=models.PROTECT,
        verbose_name='Запрос на мерч',
    )
    delivery_status = models.ForeignKey(
        DeliveryStatus,
        on_delete=models.PROTECT,
        verbose_name='Статус доставки',
    )
    assignment_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата присвоения',
    )

    class Meta:
        verbose_name = 'История доставок'
        verbose_name_plural = 'История доставок'

    def __str__(self):
        return (
            f'{self.merch_request.merch} - {self.delivery_status} - '
            f'{self.assignment_date}'
        )
