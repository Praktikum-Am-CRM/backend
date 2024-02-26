from django.db import models


class BotMessages(models.Model):
    message_id = models.ForeignKey(
        "Message",
        verbose_name="Сообщение",
        on_delete=models.CASCADE
    )
    from_bot = models.BooleanField()
    manager_id = models.ForeignKey(
        "Manager",
        verbose_name="Менеджер",
        on_delete=models.PROTECT
    )
    ambassador_id = models.ForeignKey(
        "Ambassador",
        verbose_name="Амбасадор",
        on_delete=models.CASCADE
    )
    sign_AI = models.BooleanField(
        verbose_name="Искусственный интеллект"
    )


class MessageType(models.Model):
    message_type = models.TextField()
    available = models.BooleanField()


class Message(models.Model):
    message_text = models.TextField(
        verbose_name="Текст сообщения"
    )
    media_link = models.URLField()
    date = models.DateTimeField(
        verbose_name="Дата сообщения",
        auto_now_add=True
    )
    message_type_id = models.ForeignKey(
        "MessageType",
        on_delete=models.PROTECT
    )
    message_telegram_id = models.ForeignKey(
        "BotMessages",
        verbose_name="Бот",
        on_delete=models.PROTECT
    )
    reaction = models.IntegerField()


class MessagePool(models.Model):
    message_id = models.ForeignKey(
        "Message",
        verbose_name="Сообщение",
        on_delete=models.CASCADE
    )
    message_status = models.ForeignKey(
        "MessageStatus",
        verbose_name="Статус сообщения",
        on_delete=models.PROTECT
    )
    send_date = models.DateTimeField(
        verbose_name="Дата",
        auto_now_add=True
    )


class MessageStatus(models.Model):
    message_status = models.TextField(
        verbose_name="Наименование статуса"
    )
    available = models.BooleanField()
