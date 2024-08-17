# Generated by Django 5.0.6 on 2024-07-22 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("screen_app", "0015_dailychecklistitem_monthlychecklistitem_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="monthlychecklistitem",
            name="approved_by_Supervisor",
            field=models.CharField(
                choices=[("✔", "OK"), ("✘", "Not OK"), ("", "Not Checked")],
                default="",
                max_length=100,
            ),
        ),
        migrations.AddField(
            model_name="monthlychecklistitem",
            name="checked_by_Operator",
            field=models.CharField(
                choices=[("✔", "OK"), ("✘", "Not OK"), ("", "Not Checked")],
                default="",
                max_length=100,
            ),
        ),
    ]