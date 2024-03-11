from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("merches", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deliverystatus",
            name="status_name",
            field=models.CharField(
                max_length=200, unique=True, verbose_name="Статус доставки"
            ),
        ),
        migrations.AlterField(
            model_name="merch",
            name="merch_name",
            field=models.CharField(
                max_length=200, unique=True, verbose_name="Название мерча"
            ),
        ),
    ]
