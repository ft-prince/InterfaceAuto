# Generated by Django 5.1.5 on 2025-01-19 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_app", "0006_profile_user_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="matrix",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
