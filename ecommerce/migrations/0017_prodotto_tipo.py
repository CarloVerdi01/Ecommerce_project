# Generated by Django 5.0.6 on 2024-06-14 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0016_alter_taglia_prodotto_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="prodotto",
            name="tipo",
            field=models.CharField(
                blank=True,
                choices=[
                    ("MAGLIA", "maglia"),
                    ("CAMICIA", "camicia"),
                    ("FELPA", "felpa"),
                    ("PANTALONE", "pantalone"),
                    ("GIUBBOTTO", "giubbotto"),
                ],
                max_length=30,
                null=True,
            ),
        ),
    ]
