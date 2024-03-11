from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ambassador", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity",
            name="activity_name",
            field=models.CharField(
                max_length=200, unique=True, verbose_name="Вид деятельности"
            ),
        ),
        migrations.AlterField(
            model_name="ambassador",
            name="status",
            field=models.ForeignKey(
                max_length=200,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="ambassadors",
                to="ambassador.ambassadorstatus",
                verbose_name="Статус",
            ),
        ),
        migrations.AlterField(
            model_name="ambassadoractivity",
            name="activity",
            field=models.ForeignKey(
                max_length=200,
                on_delete=django.db.models.deletion.CASCADE,
                to="ambassador.activity",
                verbose_name="Вид деятельности",
            ),
        ),
        migrations.AlterField(
            model_name="ambassadorgoal",
            name="goal",
            field=models.ForeignKey(
                max_length=200,
                on_delete=django.db.models.deletion.CASCADE,
                to="ambassador.goal",
                verbose_name="Цель",
            ),
        ),
        migrations.AlterField(
            model_name="ambassadorstatus",
            name="status_name",
            field=models.CharField(
                max_length=200, unique=True, verbose_name="Статус амбассадора"
            ),
        ),
        migrations.AlterField(
            model_name="ambassadorstatushistory",
            name="ambassador_status",
            field=models.ForeignKey(
                max_length=200,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="status_history",
                to="ambassador.ambassadorstatus",
                verbose_name="Статус",
            ),
        ),
        migrations.AlterField(
            model_name="goal",
            name="goal_name",
            field=models.CharField(
                max_length=200, unique=True, verbose_name="Название цели"
            ),
        ),
    ]
