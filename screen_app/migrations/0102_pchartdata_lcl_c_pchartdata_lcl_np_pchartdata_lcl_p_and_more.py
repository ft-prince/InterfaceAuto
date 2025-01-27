# Generated by Django 5.1.5 on 2025-01-17 07:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("screen_app", "0101_controlchartreading_lsl_controlchartreading_usl_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pchartdata",
            name="lcl_c",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pchartdata",
            name="lcl_np",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pchartdata",
            name="lcl_p",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pchartdata",
            name="lcl_u",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pchartdata",
            name="ucl_c",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pchartdata",
            name="ucl_np",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pchartdata",
            name="ucl_p",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pchartdata",
            name="ucl_u",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pchartdata",
            name="month",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="pchartdata",
            name="proportion",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
