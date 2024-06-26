# Generated by Django 5.0.6 on 2024-06-13 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0008_prodotto_sesso_prodotto_tipo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prodotto",
            name="tipo",
            field=models.CharField(
                choices=[
                    ("ABBIGLIAMENTO", "abbigliamento"),
                    ("SCARPE", "scarpe"),
                    ("PROFUMO", "profumo"),
                    ("ACCESSORIO", "accessorio"),
                ],
                default="ABBIGLIAMENTO",
                max_length=30,
            ),
        ),
    ]
