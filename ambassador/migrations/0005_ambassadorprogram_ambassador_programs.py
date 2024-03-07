# Generated by Django 4.2.7 on 2024-03-06 06:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("program", "0003_delete_ambassadorprogram"),
        (
            "ambassador",
            "0004_alter_ambassador_manager_alter_ambassador_status_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="AmbassadorProgram",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "ambassador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="ambassador.ambassador",
                    ),
                ),
                (
                    "program",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="ambassadors",
                        to="program.program",
                    ),
                ),
            ],
            options={
                "verbose_name": "Программа амбассадоров",
                "verbose_name_plural": "Программы амбассадоров",
            },
        ),
        migrations.AddField(
            model_name="ambassador",
            name="programs",
            field=models.ManyToManyField(
                blank=True,
                related_name="programs",
                through="ambassador.AmbassadorProgram",
                to="program.program",
            ),
        ),
    ]