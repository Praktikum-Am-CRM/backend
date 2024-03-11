from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm_messages", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="messagestatus",
            name="status_name",
            field=models.CharField(
                max_length=200,
                unique=True,
                verbose_name="Наименование статуса",
            ),
        ),
        migrations.AlterField(
            model_name="messagetype",
            name="type_name",
            field=models.CharField(
                max_length=200, unique=True, verbose_name="Тип сообщения"
            ),
        ),
    ]
