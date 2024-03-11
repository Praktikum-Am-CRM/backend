from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ambassador", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("merches", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="merchrequest",
            name="manager",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="merch_requests",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Менеджер",
            ),
        ),
        migrations.AddField(
            model_name="merchrequest",
            name="merch",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="merch_requests",
                to="merches.merch",
                verbose_name="Мерч",
            ),
        ),
        migrations.AddField(
            model_name="merchrequest",
            name="request_status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="merch_requests",
                to="merches.deliverystatus",
                verbose_name="Статус выполнения",
            ),
        ),
        migrations.AddField(
            model_name="deliveryhistory",
            name="delivery_status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="delivery_history",
                to="merches.deliverystatus",
                verbose_name="Статус доставки",
            ),
        ),
        migrations.AddField(
            model_name="deliveryhistory",
            name="merch_request",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="delivery_history",
                to="merches.merchrequest",
                verbose_name="Запрос на мерч",
            ),
        ),
        migrations.AddField(
            model_name="ambassadorrequest",
            name="ambassador",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="requests",
                to="ambassador.ambassador",
            ),
        ),
        migrations.AddField(
            model_name="ambassadorrequest",
            name="merch_request",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="ambassadors",
                to="merches.merchrequest",
            ),
        ),
    ]
