# Generated by Django 4.2.7 on 2024-03-01 12:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("telegram", "0001_initial"),
        ("ambassador", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ambassador",
            name="manager",
            field=models.ForeignKey(
                blank=True,
                max_length=50,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Менеджер",
            ),
        ),
        migrations.AddField(
            model_name="ambassador",
            name="status",
            field=models.ForeignKey(
                max_length=50,
                on_delete=django.db.models.deletion.PROTECT,
                to="ambassador.ambassadorstatus",
                verbose_name="Статус",
            ),
        ),
        migrations.AddField(
            model_name="ambassador",
            name="telegram_bot",
            field=models.ForeignKey(
                max_length=50,
                on_delete=django.db.models.deletion.PROTECT,
                to="telegram.telegrambot",
                verbose_name="Телеграмм бот",
            ),
        ),
    ]