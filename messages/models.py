from django.db import models


class Answer(models.Model):
    id = models.UUIDField(primary_key=True)
    ambassador = models.ForeignKey(
        "Ambassador",
        verbose_name="Амбассадо",
        on_delete=models.CASCADE
    )
    message = models.ForeignKey(
        "Messages",
        verbose_name="Сообщение",
        on_delete=models.PROTECT
    )
    answer_text = models.TextField(verbose_name="Текст ответа")
    answer_dispath_time = models.DateTimeField(
        verbose_name="Дата и время сообщения",
        auto_now_add=True
    )
    reaction = models.CharField(verbose_name="Реакция")
    sign_artificial_intelligence = models.BooleanField(default=False)


class ReplyMessage(models.Model):
    message = models.ForeignKey(
        "Messages",
        verbose_name="Сообщение",
        on_delete=models.PROTECT
    )
    answer = models.ForeignKey(
        "Anaswer",
        verbose_name="Ответ",
        on_delete=models.PROTECT
    )


class Messages(models.Model):
    id = models.UUIDField(primary_key=True)
    message_text = models.TextField(verbose_name="Текст сообщения")
    message_dispath_time = models.DateField(auto_now_add=True)
    answer = models.ForeignKey(
        "Anaswer",
        verbose_name="Ответ",
        blank=True,
        on_delete=models.PROTECT
    )


class MessagesAmbassador(models.Model):
    message = models.ForeignKey(
        "Messages",
        verbose_name="Сообщение",
        on_delete=models.PROTECT
    )
    ambassador = models.ForeignKey(
        "Ambassador",
        verbose_name="Амбассадо",
        on_delete=models.CASCADE
    )


class Messages_Status(models.Model):
    STATUS_LIST = (
        ("черновик", "черновик"),
        ("шаблон", "шаблон"),
        ("отложенная", "отложенная"),
    )
    id = models.UUIDField(primary_key=True)
    message_statis = models.CharField(
        verbose_name="Статус",
        choices=STATUS_LIST,
    )


class Messages_Type(models.Model):
    TYPE_LIST = (
        ("Анкета", "Анкета"),
        ("Отчет", "Отчет по гайду"),
        ("Подтверждение", "Подтверждение адреса"),
        ("Вопрос", "Вопрос"),
        ("Запрос", "Запрос на изменение данных"),
    )
    id = models.UUIDField(primary_key=True)
    message_type = models.CharField(
        verbose_name="Тип ответа",
        choices=TYPE_LIST
    )
