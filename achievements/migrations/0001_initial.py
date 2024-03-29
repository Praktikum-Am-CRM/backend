from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Achieve",
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
                    "achieve_name",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        verbose_name="Название ачивки",
                    ),
                ),
                (
                    "available",
                    models.BooleanField(default=True, verbose_name="Доступна"),
                ),
            ],
            options={
                "verbose_name": "Ачивки",
                "verbose_name_plural": "Ачивки",
            },
        ),
    ]
