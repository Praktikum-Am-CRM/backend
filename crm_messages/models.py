import uuid

from django.db import models

from ambassador.models import Ambassador
from users.models import Manager


class BotMessages(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True
    )
    message_id = models.ForeignKey(
        "Message",
        verbose_name="Сообщение",
        max_length=50,
        on_delete=models.CASCADE,
    )
    from_bot = models.BooleanField()
    manager_id = models.ForeignKey(
        Manager,
        verbose_name="Менеджер",
        max_length=50,
        on_delete=models.PROTECT,
    )
    ambassador_id = models.ForeignKey(
        Ambassador,
        verbose_name="Амбасадор",
        max_length=50,
        on_delete=models.CASCADE,
    )
    sign_ai = models.BooleanField(verbose_name="Искусственный интеллект")


class MessageType(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True
    )
    type_name = models.CharField(max_length=250)
    available = models.BooleanField()


class Message(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True
    )
    message_text = models.CharField(
        verbose_name="Текст сообщения", max_length=250
    )
    media_link = models.FileField()
    date = models.DateTimeField(
        verbose_name="Дата сообщения", auto_now_add=True
    )
    message_type_id = models.ForeignKey(
        "MessageType", max_length=50, on_delete=models.PROTECT
    )


class MessagePool(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True
    )
    message_id = models.ForeignKey(
        "Message", verbose_name="Сообщение", on_delete=models.CASCADE
    )
    message_status = models.ForeignKey(
        "MessageStatus",
        verbose_name="Статус сообщения",
        max_length=50,
        on_delete=models.PROTECT,
    )
    send_date = models.DateTimeField(verbose_name="Дата", auto_now_add=True)


class MessageStatus(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True
    )
    status_name = models.CharField(
        verbose_name="Наименование статуса", max_length=250
    )
    available = models.BooleanField()
