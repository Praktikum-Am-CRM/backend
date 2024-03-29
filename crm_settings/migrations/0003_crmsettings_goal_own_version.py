from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ambassador", "0002_initial"),
        ("crm_settings", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="crmsettings",
            name="goal_own_version",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="ambassador.goal",
            ),
        ),
    ]
