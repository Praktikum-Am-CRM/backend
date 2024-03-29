from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ambassador", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "message_text",
                    models.CharField(
                        max_length=250, verbose_name="Текст сообщения"
                    ),
                ),
                (
                    "media_link",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="messages/",
                        verbose_name="Медиа файл",
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата сообщения"
                    ),
                ),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
            },
        ),
        migrations.CreateModel(
            name="MessageStatus",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "status_name",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        verbose_name="Наименование статуса",
                    ),
                ),
                (
                    "available",
                    models.BooleanField(
                        default=True, verbose_name="Доступность"
                    ),
                ),
            ],
            options={
                "verbose_name": "Статус сообщения",
                "verbose_name_plural": "Статусы сообщения",
            },
        ),
        migrations.CreateModel(
            name="MessageType",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "type_name",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        verbose_name="Тип сообщения",
                    ),
                ),
                (
                    "available",
                    models.BooleanField(
                        default=True, verbose_name="Доступность"
                    ),
                ),
            ],
            options={
                "verbose_name": "Тип сообщения",
                "verbose_name_plural": "Типы сообщения",
            },
        ),
        migrations.CreateModel(
            name="MessagePool",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "send_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Когда отправить сообщение",
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="messages_pool",
                        to="crm_messages.message",
                        verbose_name="Сообщение",
                    ),
                ),
                (
                    "message_status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="messages_pool",
                        to="crm_messages.messagestatus",
                    ),
                ),
            ],
            options={
                "verbose_name": "Служебное сообщение",
                "verbose_name_plural": "Служебные сообщения",
            },
        ),
        migrations.AddField(
            model_name="message",
            name="message_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="messages",
                to="crm_messages.messagetype",
            ),
        ),
        migrations.CreateModel(
            name="BotMessages",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("from_bot", models.BooleanField()),
                (
                    "sign_ai",
                    models.BooleanField(
                        verbose_name="Искусственный интеллект"
                    ),
                ),
                (
                    "message_telegram_id",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=50,
                        verbose_name="Номер сообщения в телеграм",
                    ),
                ),
                (
                    "reaction",
                    models.IntegerField(
                        choices=[
                            (-1, "Дизлайк"),
                            (0, "Нет реакции"),
                            (1, "Лайк"),
                        ],
                        default=0,
                        verbose_name="Реация на сообщение",
                    ),
                ),
                (
                    "ambassador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="bot_messages",
                        to="ambassador.ambassador",
                        verbose_name="Амбасcадор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Сообщение телеграм бота",
                "verbose_name_plural": "Сообщения телеграм бота",
            },
        ),
    ]
