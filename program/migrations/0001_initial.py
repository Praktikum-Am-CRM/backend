from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Program",
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
                    "program_name",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        verbose_name="Название программы обучения",
                    ),
                ),
                (
                    "available",
                    models.BooleanField(default=True, verbose_name="Доступна"),
                ),
            ],
            options={
                "verbose_name": "Программа",
                "verbose_name_plural": "Программы",
            },
        ),
    ]
