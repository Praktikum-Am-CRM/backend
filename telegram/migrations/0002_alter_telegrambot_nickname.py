# Generated by Django 4.2.7 on 2024-03-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("telegram", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="telegrambot",
            name="nickname",
            field=models.CharField(
                max_length=200, verbose_name="Telegram Username"
            ),
        ),
    ]