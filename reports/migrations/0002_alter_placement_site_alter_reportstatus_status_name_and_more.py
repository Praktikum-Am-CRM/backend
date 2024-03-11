from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="placement",
            name="site",
            field=models.CharField(
                max_length=200,
                unique=True,
                verbose_name="Площадка размещения контента",
            ),
        ),
        migrations.AlterField(
            model_name="reportstatus",
            name="status_name",
            field=models.CharField(
                max_length=200, unique=True, verbose_name="Статус отчета"
            ),
        ),
        migrations.AlterField(
            model_name="reporttype",
            name="type_name",
            field=models.CharField(
                max_length=200, unique=True, verbose_name="Вид задания"
            ),
        ),
    ]
