# Generated by Django 4.2.7 on 2024-03-05 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("achievements", "0003_alter_ambassadorachieve_achieve_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ambassadorachieve",
            name="achieve",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="ambassadors",
                to="achievements.achieve",
            ),
        ),
    ]