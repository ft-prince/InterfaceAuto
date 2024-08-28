# Generated by Django 5.1 on 2024-08-27 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("screen_app", "0081_alter_startupchecksheet_process_operation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="startupchecksheet",
            name="process_operation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="screen_app.machinelocation",
                verbose_name="Process/Operation",
            ),
        ),
    ]