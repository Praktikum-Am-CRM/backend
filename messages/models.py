from django.db import models
import uuid

class BotMessages(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        unique=True
    )
    message_id = models.ForeignKey(
        "Message",
        verbose_name="Сообщение",
        max_length=50,
        on_delete=models.CASCADE
    )
    from_bot = models.BooleanField()
    manager_id = models.ForeignKey(
        "Manager",
        verbose_name="Менеджер",
        max_length=50,
        on_delete=models.PROTECT
    )
    ambassador_id = models.ForeignKey(
        "Ambassador",
        verbose_name="Амбасадор",
        max_length=50,
        on_delete=models.CASCADE
    )
    sign_ai = models.BooleanField(
        verbose_name="Искусственный интеллект"
    )


class MessageType(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        unique=True
    )
    message_type = models.CharField(
        max_length=250
    )
    available = models.BooleanField()


class Message(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        unique=True
    )
    message_text = models.CharField(
        verbose_name="Текст сообщения",
        max_length=250
    )
    media_link = models.FileField()
    date = models.DateTimeField(
        verbose_name="Дата сообщения",
        auto_now_add=True
    )
    message_type_id = models.ForeignKey(
        "MessageType",
        max_length=50,
        on_delete=models.PROTECT
    )
    message_telegram_id = models.ForeignKey(
        "BotMessages",
        verbose_name="Бот",
        max_length=50,
        on_delete=models.PROTECT
    )
    reaction = models.IntegerField(max_length=2)


class MessagePool(models.Model):
    message_id = models.ForeignKey(
        "Message",
        verbose_name="Сообщение",
        on_delete=models.CASCADE
    )
    message_status = models.ForeignKey(
        "MessageStatus",
        verbose_name="Статус сообщения",
        max_length=50,
        on_delete=models.PROTECT
    )
    send_date = models.DateTimeField(
        verbose_name="Дата",
        auto_now_add=True
    )


class MessageStatus(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        unique=True
    )
    message_status = models.CharField(
        verbose_name="Наименование статуса",
        max_length=250
    )
    available = models.BooleanField()