from django.contrib import admin
from .models import Prodotto
from .models import Taglia
from .models import Ordine
from .models import DettaglioOrdine
from .models import Carrello

admin.site.register(Prodotto)
admin.site.register(Taglia)
admin.site.register(Ordine)
admin.site.register(DettaglioOrdine)
admin.site.register(Carrello)


# Register your models here.

