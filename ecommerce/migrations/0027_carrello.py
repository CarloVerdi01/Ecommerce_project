# Generated by Django 5.0.6 on 2024-06-15 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0026_alter_taglia_quantità"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carrello",
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
                (
                    "taglia",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("XS", "xs"),
                            ("S", "s"),
                            ("M", "m"),
                            ("L", "l"),
                            ("XL", "xl"),
                        ],
                        max_length=30,
                        null=True,
                    ),
                ),
                (
                    "numero",
                    models.DecimalField(
                        blank=True, decimal_places=1, max_digits=7, null=True
                    ),
                ),
                ("prezzo", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantita", models.PositiveIntegerField(default=1)),
                (
                    "prodotto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecommerce.prodotto",
                    ),
                ),
                (
                    "utente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="carrello",
                        to="ecommerce.utente",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Carrelli",
            },
        ),
    ]
