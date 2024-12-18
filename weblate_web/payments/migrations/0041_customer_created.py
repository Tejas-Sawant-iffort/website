# Generated by Django 5.1.3 on 2024-12-18 10:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0040_fill_in_users"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
