from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("crm_settings", "0001_initial"),
        ("reports", "0001_initial"),
        ("merches", "0001_initial"),
        ("crm_messages", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="crmsettings",
            name="default_delivery_status",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                to="merches.deliverystatus",
            ),
        ),
        migrations.AddField(
            model_name="crmsettings",
            name="default_message_status",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="default_message_status",
                to="crm_messages.messagestatus",
            ),
        ),
        migrations.AddField(
            model_name="crmsettings",
            name="default_message_type",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="crm_messages.messagetype",
            ),
        ),
        migrations.AddField(
            model_name="crmsettings",
            name="default_report_status",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="reports.reportstatus",
            ),
        ),
        migrations.AddField(
            model_name="crmsettings",
            name="default_report_type",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="reports.reporttype",
            ),
        ),
        migrations.AddField(
            model_name="crmsettings",
            name="delayed_sending_message_type",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="delayed_sending_message_type",
                to="crm_messages.messagestatus",
            ),
        ),
    ]
