import uuid

from django.db import models

from ambassador.models import Ambassador
from users.models import Manager

MESSAGE_REACTION = (
    (-1, 'Дизлайк'),
    (0, 'Нет реакции'),
    (1, 'Лайк'),
)


class BotMessages(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True
    )
    message = models.ForeignKey(
        'Message',
        verbose_name='Сообщение',
        on_delete=models.PROTECT,
        related_name='bot_messages',
    )
    from_bot = models.BooleanField()
    manager = models.ForeignKey(
        Manager,
        verbose_name='Менеджер',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='bot_messages',
    )
    ambassador = models.ForeignKey(
        Ambassador,
        verbose_name='Амбасcадор',
        on_delete=models.PROTECT,
        related_name='bot_messages',
    )
    sign_ai = models.BooleanField(verbose_name='Искусственный интеллект')
    message_telegram_id = models.CharField(
        max_length=50,
        verbose_name='Номер сообщения в телеграм',
        null=False,
        blank=True,
        default='',
    )
    reaction = models.IntegerField(
        verbose_name='Реация на сообщение',
        choices=MESSAGE_REACTION,
        null=False,
        default=0,
    )

    class Meta:
        verbose_name = 'Сообщение телеграм бота'
        verbose_name_plural = 'Сообщения телеграм бота'

    def __str__(self):
        return (
            f'{self.ambassador if self.from_bot else self.manager} -'
            f' {self.message}'
        )


class MessageType(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True
    )
    type_name = models.CharField(
        max_length=50, verbose_name='Тип ' 'сообщения', unique=True
    )
    available = models.BooleanField(default=True, verbose_name='Доступность')

    class Meta:
        verbose_name = 'Тип сообщения'
        verbose_name_plural = 'Типы сообщения'

    def __str__(self):
        return f'{self.type_name}'


class Message(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True
    )
    message_text = models.CharField(
        verbose_name='Текст сообщения', max_length=250
    )
    media_link = models.FileField(
        verbose_name='Медиа файл', upload_to='messages/', null=True, blank=True
    )
    date = models.DateTimeField(
        verbose_name='Дата сообщения',
        blank=True,
        null=True,
    )
    message_type = models.ForeignKey(
        'MessageType',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='messages',
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'{self.message_text[:30]}'


class MessagePool(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True
    )
    message = models.ForeignKey(
        'Message',
        verbose_name='Сообщение',
        on_delete=models.PROTECT,
        related_name='messages_pool',
    )
    message_status = models.ForeignKey(
        'MessageStatus', on_delete=models.PROTECT, related_name='messages_pool'
    )
    send_date = models.DateTimeField(
        verbose_name='Когда отправить сообщение',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Служебное сообщение'
        verbose_name_plural = 'Служебные сообщения'

    def __str__(self):
        return (
            f'{self.message_status} - '
            f'{self.message}'
            f' - {self.send_date}'
            if self.send_date
            else ''
        )


class MessageStatus(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True
    )
    status_name = models.CharField(
        verbose_name='Наименование статуса', max_length=50, unique=True
    )
    available = models.BooleanField(default=True, verbose_name='Доступность')

    class Meta:
        verbose_name = 'Статус сообщения'
        verbose_name_plural = 'Статусы сообщения'

    def __str__(self):
        return f'{self.status_name}'
