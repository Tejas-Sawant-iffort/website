# Generated by Django 5.1.3 on 2024-11-27 09:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("weblate_web", "0033_service_backup_box_service_backup_directory"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="backup_size",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="service",
            name="backup_timestamp",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
