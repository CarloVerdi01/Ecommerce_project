# Generated by Django 5.0.6 on 2024-06-10 13:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "ecommerce",
            "0002_alter_dettaglioordine_options_alter_ordine_options_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ProfiloUtente",
            new_name="Utente",
        ),
        migrations.AlterModelOptions(
            name="utente",
            options={"verbose_name_plural": "Utenti"},
        ),
    ]
