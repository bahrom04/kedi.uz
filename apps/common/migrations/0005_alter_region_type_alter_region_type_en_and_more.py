# Generated by Django 5.0.3 on 2024-04-13 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0004_alter_event_title_alter_event_title_en_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="region",
            name="type",
            field=models.CharField(
                max_length=255, unique=True, verbose_name="Street name (Arentir)"
            ),
        ),
        migrations.AlterField(
            model_name="region",
            name="type_en",
            field=models.CharField(
                max_length=255,
                null=True,
                unique=True,
                verbose_name="Street name (Arentir)",
            ),
        ),
        migrations.AlterField(
            model_name="region",
            name="type_ru",
            field=models.CharField(
                max_length=255,
                null=True,
                unique=True,
                verbose_name="Street name (Arentir)",
            ),
        ),
        migrations.AlterField(
            model_name="region",
            name="type_uz",
            field=models.CharField(
                max_length=255,
                null=True,
                unique=True,
                verbose_name="Street name (Arentir)",
            ),
        ),
    ]
