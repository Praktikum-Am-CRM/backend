# Generated by Django 4.2.7 on 2024-02-29 05:44

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ambassador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
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
                        auto_now_add=True,
                        verbose_name="Дата запуска бота пользователем",
                    ),
                ),
                ("active", models.BooleanField(default=True)),
            ],
        ),
    ]
