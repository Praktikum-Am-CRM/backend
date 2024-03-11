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
