# Generated by Django 4.2.7 on 2024-03-06 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ambassador", "0005_ambassadorprogram_ambassador_programs"),
    ]

    operations = [
        migrations.AddField(
            model_name="ambassador",
            name="activity",
            field=models.ManyToManyField(
                blank=True,
                related_name="goals",
                through="ambassador.AmbassadorActivity",
                to="ambassador.activity",
            ),
        ),
        migrations.AddField(
            model_name="ambassador",
            name="goals",
            field=models.ManyToManyField(
                blank=True,
                related_name="goals",
                through="ambassador.AmbassadorGoal",
                to="ambassador.goal",
            ),
        ),
        migrations.AlterField(
            model_name="ambassadoractivity",
            name="activity",
            field=models.ForeignKey(
                max_length=50,
                on_delete=django.db.models.deletion.CASCADE,
                to="ambassador.activity",
                verbose_name="Вид деятельности",
            ),
        ),
        migrations.AlterField(
            model_name="ambassadoractivity",
            name="ambassador",
            field=models.ForeignKey(
                max_length=50,
                on_delete=django.db.models.deletion.CASCADE,
                to="ambassador.ambassador",
                verbose_name="Амбассадор",
            ),
        ),
        migrations.AlterField(
            model_name="ambassadorgoal",
            name="ambassador",
            field=models.ForeignKey(
                max_length=50,
                on_delete=django.db.models.deletion.CASCADE,
                to="ambassador.ambassador",
                verbose_name="Амбассадор",
            ),
        ),
        migrations.AlterField(
            model_name="ambassadorgoal",
            name="goal",
            field=models.ForeignKey(
                max_length=50,
                on_delete=django.db.models.deletion.CASCADE,
                to="ambassador.goal",
                verbose_name="Цель",
            ),
        ),
    ]