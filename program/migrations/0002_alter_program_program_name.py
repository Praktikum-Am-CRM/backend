from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("program", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="program",
            name="program_name",
            field=models.CharField(
                max_length=200,
                unique=True,
                verbose_name="Название программы обучения",
            ),
        ),
    ]
