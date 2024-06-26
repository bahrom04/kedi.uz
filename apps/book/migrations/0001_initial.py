# Generated by Django 5.0.3 on 2024-06-30 04:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Community",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128, verbose_name="Title")),
                (
                    "title_uz",
                    models.CharField(max_length=128, null=True, verbose_name="Title"),
                ),
                (
                    "title_ru",
                    models.CharField(max_length=128, null=True, verbose_name="Title"),
                ),
                (
                    "title_en",
                    models.CharField(max_length=128, null=True, verbose_name="Title"),
                ),
                ("image", models.ImageField(upload_to="community/")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "description_uz",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "description_ru",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "description_en",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                ("telegram_link", models.URLField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
