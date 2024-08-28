# Generated by Django 5.1 on 2024-08-24 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("screen_app", "0076_alter_solderingbitrecord_machine_no"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rejectionsheet",
            name="part_description",
            field=models.CharField(
                choices=[
                    ("DSL01_S01", "DSL01_S01"),
                    ("DSL01_S02", "DSL01_S02"),
                    ("DSL01_S03", "DSL01_S03"),
                    ("DSL01_S04", "DSL01_S04"),
                    ("DSL01_S05", "DSL01_S05"),
                    ("DSL01_S06", "DSL01_S06"),
                    ("DSL01_S07", "DSL01_S07"),
                    ("DSL01_S08", "DSL01_S08"),
                    ("DSL01_S09", "DSL01_S09"),
                ],
                max_length=250,
            ),
        ),
        migrations.AlterField(
            model_name="rejectionsheet",
            name="stage",
            field=models.CharField(
                choices=[
                    ("DSL01_S01", "DSL01_S01"),
                    ("DSL01_S02", "DSL01_S02"),
                    ("DSL01_S03", "DSL01_S03"),
                    ("DSL01_S04", "DSL01_S04"),
                    ("DSL01_S05", "DSL01_S05"),
                    ("DSL01_S06", "DSL01_S06"),
                    ("DSL01_S07", "DSL01_S07"),
                    ("DSL01_S08", "DSL01_S08"),
                    ("DSL01_S09", "DSL01_S09"),
                ],
                max_length=200,
            ),
        ),
    ]