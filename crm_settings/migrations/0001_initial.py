from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ambassador", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CrmSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "default_ambassador_status",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="ambassador.ambassadorstatus",
                    ),
                ),
            ],
            options={
                "ordering": ("-date",),
            },
        ),
    ]
