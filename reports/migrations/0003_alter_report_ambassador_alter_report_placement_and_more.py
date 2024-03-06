# Generated by Django 4.2.7 on 2024-03-05 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "ambassador",
            "0004_alter_ambassador_manager_alter_ambassador_status_and_more",
        ),
        ("reports", "0002_alter_report_report_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="ambassador",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="reports",
                to="ambassador.ambassador",
            ),
        ),
        migrations.AlterField(
            model_name="report",
            name="placement",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="reports",
                to="reports.placement",
            ),
        ),
        migrations.AlterField(
            model_name="report",
            name="report_status",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="reports",
                to="reports.reportstatus",
            ),
        ),
        migrations.AlterField(
            model_name="report",
            name="report_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="reports",
                to="reports.reporttype",
            ),
        ),
    ]
