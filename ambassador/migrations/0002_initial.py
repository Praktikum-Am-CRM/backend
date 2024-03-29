from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("program", "0001_initial"),
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
                related_name="ambassadors",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Менеджер",
            ),
        ),
        migrations.AddField(
            model_name="ambassador",
            name="programs",
            field=models.ManyToManyField(
                related_name="programs",
                through="ambassador.AmbassadorProgram",
                to="program.program",
            ),
        ),
        migrations.AddField(
            model_name="ambassador",
            name="status",
            field=models.ForeignKey(
                max_length=50,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="ambassadors",
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
                related_name="ambassadors",
                to="telegram.telegrambot",
                verbose_name="Телеграмм бот",
            ),
        ),
    ]
