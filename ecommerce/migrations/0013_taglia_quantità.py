# Generated by Django 5.0.6 on 2024-06-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0012_alter_prodotto_tipo"),
    ]

    operations = [
        migrations.AddField(
            model_name="taglia",
            name="quantità",
            field=models.DecimalField(decimal_places=0, default=1, max_digits=7),
        ),
    ]
