# Generated by Django 5.1.3 on 2024-11-29 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0040_fill_in_users"),
        ("weblate_web", "0035_alter_service_backup_size"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="donation",
            name="user",
        ),
        migrations.RemoveField(
            model_name="service",
            name="users",
        ),
        migrations.AlterField(
            model_name="donation",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="payments.customer"
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="payments.customer"
            ),
        ),
    ]
