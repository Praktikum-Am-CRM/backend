from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("achievements", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="achieve",
            name="achieve_name",
            field=models.CharField(
                max_length=200, unique=True, verbose_name="Название ачивки"
            ),
        ),
    ]
