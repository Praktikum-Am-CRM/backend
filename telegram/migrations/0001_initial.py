from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TelegramBot",
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
                    "telegram_id",
                    models.CharField(
                        max_length=100, verbose_name="Telegram chat ID"
                    ),
                ),
                (
                    "nickname",
                    models.CharField(
                        max_length=100, verbose_name="Telegram Username"
                    ),
                ),
                (
                    "registration_date",
                    models.DateTimeField(
                        verbose_name="Дата запуска бота пользователем"
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        default=True, verbose_name="Активный?"
                    ),
                ),
            ],
            options={
                "verbose_name": "Данные амбассадора в телеграм",
                "verbose_name_plural": "Данные амбассадора в телеграм",
            },
        ),
    ]
