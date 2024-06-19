from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser






class Prodotto(models.Model):
    SESSO_PRODOTTO = [
        ('M', 'm'),
        ('F', 'f'),
        ('UNISEX','unisex'),
    ]

    CATEGORIA_PRODOTTO = [
        ('ABBIGLIAMENTO', 'abbigliamento'),
        ('SCARPE', 'scarpe'),
        ('PROFUMO', 'profumo'),
        ('ACCESSORIO', 'accessorio')
    ]

    TIPO_PRODOTTO = [
        ('MAGLIA', 'maglia'),
        ('CAMICIA', 'camicia'),
        ('FELPA', 'felpa'),
        ('PANTALONE', 'pantalone'),
        ('GIUBBOTTO', 'giubbotto')

    ]


    id = models.CharField(max_length=15, primary_key=True)
    nome = models.CharField(max_length=30)
    descrizione = models.TextField(blank=True, null=True)
    prezzo = models.DecimalField(max_digits=7, decimal_places=2)
    immagine = models.ImageField(upload_to='prodotti', default='https://placehold.co/600x400')
    sesso = models.CharField(max_length=30, choices=SESSO_PRODOTTO, default='UNISEX')
    categoria = models.CharField(max_length=30, choices=CATEGORIA_PRODOTTO, default="ABBIGLIAMENTO")
    tipo = models.CharField(max_length=30, choices=TIPO_PRODOTTO, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Prodotti"




class Taglia(models.Model):
    TAGLIA = [
        ('XS', 'xs'),
        ('S', 's'),
        ('M', 'm'),
        ('L', 'l'),
        ('XL', 'xl'),
    ]


    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE, related_name='taglie')
    taglia = models.CharField(max_length=30, choices=TAGLIA, blank=True, null=True)
    numero = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    quantità = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Taglie"



    def __str__(self):
        if self.taglia is not None:
            return f"{self.prodotto.nome} - Taglia {self.taglia}"
        else:
            return f"{self.prodotto.nome} - Numero {self.numero}"







class Ordine(models.Model):
    utente = models.ForeignKey(User , on_delete=models.CASCADE)
    data_ordine = models.DateTimeField(auto_now_add=True)
    indirizzo_spedizione = models.CharField(max_length=100)
    stato_ordine = models.CharField(max_length=20, choices=[('IN_ATTESA', 'In Attesa'), ('IN_TRANSITO', 'In Transito'),
                                                            ('CONSEGNATO', 'Consegnato'), ('ANNULLATO', 'annullato')])
    metodo_pagamento = models.CharField(max_length=20)
    numero_tracciamento = models.CharField(max_length=50, blank=True, null=True)
    note_aggiuntive = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Ordini"



class DettaglioOrdine(models.Model):
    ordine = models.ForeignKey(Ordine, on_delete=models.CASCADE)
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    quantita = models.PositiveIntegerField()
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)
    taglia = models.CharField(max_length=30, blank=True, null=True)
    numero = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)  # Aggiungi il campo numero


    class Meta:
        verbose_name_plural = "DettagliOrdini"

class Carrello(models.Model):

    utente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carrello')
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    taglia = models.CharField(max_length=30, choices=Taglia.TAGLIA, blank=True, null=True)
    numero = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)
    quantita = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = "Carrelli"

    def __str__(self):
        return f"{self.utente} "



