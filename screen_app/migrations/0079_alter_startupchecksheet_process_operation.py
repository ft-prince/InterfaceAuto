# Generated by Django 5.1 on 2024-08-27 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("screen_app", "0078_machinelocation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="startupchecksheet",
            name="process_operation",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="screen_app.machinelocation",
                verbose_name="Process/Operation",
            ),
        ),
    ]