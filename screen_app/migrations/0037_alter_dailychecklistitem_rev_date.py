# Generated by Django 5.0.6 on 2024-08-15 07:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("screen_app", "0036_alter_dailychecklistitem_station"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailychecklistitem",
            name="rev_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]