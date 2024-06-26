# Generated by Django 5.0.6 on 2024-06-13 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0010_prodotto_categoria_alter_prodotto_tipo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prodotto",
            name="tipo",
            field=models.CharField(
                blank=True,
                choices=[
                    ("MAGLIA", "maglia"),
                    ("CAMICIA", "camicia"),
                    ("PANTALONE", "pantalone"),
                    ("GIUBBOTTO", "giubbotto"),
                ],
                max_length=30,
                null=True,
            ),
        ),
    ]
