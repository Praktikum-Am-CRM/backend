# Generated by Django 4.2.7 on 2024-02-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_manager_email_alter_manager_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="manager",
            name="first_name",
            field=models.CharField(max_length=255, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="manager",
            name="last_name",
            field=models.CharField(max_length=255, verbose_name="Фамилия"),
        ),
    ]
