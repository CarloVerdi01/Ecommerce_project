# Generated by Django 5.0.6 on 2024-06-14 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0021_numero"),
    ]

    operations = [
        migrations.CreateModel(
            name="Giorni",
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
                ("giorno", models.CharField(max_length=20)),
            ],
        ),
    ]