# Generated by Django 4.2.7 on 2024-03-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm_messages", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата сообщения"
            ),
        ),
    ]
