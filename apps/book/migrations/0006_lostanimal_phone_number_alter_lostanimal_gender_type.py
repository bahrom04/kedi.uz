# Generated by Django 4.2 on 2024-10-23 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0005_gendertype_lostanimal_gender_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="lostanimal",
            name="phone_number",
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="lostanimal",
            name="gender_type",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="book.gendertype",
            ),
            preserve_default=False,
        ),
    ]