from django.urls import path
from .views import home_view
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home_view, name='home'),
    path('lista_prodotti_uomo/', views.lista_prodotti_uomo_view, name='lista_prodotti_uomo'),
    path('lista_prodotti_donna/', views.lista_prodotti_donna_view, name='lista_prodotti_donna'),
    path('lista_prodotti/', views.lista_prodotti_abbigliamento_view, name='lista_prodotti_abbigliamento'),
    path('lista_scarpe/', views.lista_scarpe_view, name='lista_scarpe'),
    path('lista_accessori/', views.lista_accessori_view, name='lista_accessori'),
    path('lista_profumi/', views.lista_profumi_view, name='lista_profumi'),
    path('lista_profumi_uomo/', views.lista_profumi_uomo_view, name='lista_profumi_uomo'),
    path('lista_accessori_uomo/', views.lista_accessori_uomo_view, name='lista_accessori_uomo'),
    path('lista_scarpe_uomo/', views.lista_scarpe_uomo_view, name='lista_scarpe_uomo'),
    path('lista_profumi_donna/', views.lista_profumi_donna_view, name='lista_profumi_donna'),
    path('lista_accessori_donna/', views.lista_accessori_donna_view, name='lista_accessori_donna'),
    path('lista_scarpe_donna/', views.lista_scarpe_donna_view, name='lista_scarpe_donna'),
    path('lista_abbigliamento_uomo/', views.lista_abbigliamento_uomo_view, name='lista_abbigliamento_uomo'),
    path('lista_abbigliamento_donna/', views.lista_abbigliamento_donna_view, name='lista_abbigliamento_donna'),
    path('lista_maglie_uomo/', views.lista_maglie_uomo_view, name='lista_maglie_uomo'),
    path('lista_camicie_uomo/', views.lista_camicie_uomo_view, name='lista_camicie_uomo'),
    path('lista_felpe_uomo/', views.lista_felpe_uomo_view, name='lista_felpe_uomo'),
    path('lista_pantaloni_uomo/', views.lista_pantaloni_uomo_view, name='lista_pantaloni_uomo'),
    path('lista_giubbotti_uomo/', views.lista_giubbotti_uomo_view, name='lista_giubbotti_uomo'),
    path('lista_maglie_donna/', views.lista_maglie_donna_view, name='lista_maglie_donna'),
    path('lista_camicie_donna/', views.lista_camicie_donna_view, name='lista_camicie_donna'),
    path('lista_felpe_donna/', views.lista_felpe_donna_view, name='lista_felpe_donna'),
    path('lista_pantaloni_donna/', views.lista_pantaloni_donna_view, name='lista_pantaloni_donna'),
    path('lista_giubbotti_donna/', views.lista_giubbotti_donna_view, name='lista_giubbotti_donna'),
    path('chi_siamo/', views.chi_siamo_view, name='chi_siamo'),
    path('termini_legali_e_privacy/', views.termini_legali_e_privacy_view, name='termini_legali_e_privacy'),
    path('contatti/', views.contatti_view, name='contatti'),
    path('cookie/', views.cookie_view, name='cookie'),
    path('prodotto/<int:prodotto_id>/', views.dettagli_prodotto_view, name='dettagli_prodotto'),
    path('carrello/', views.carrello_view, name='carrello'),
    path('login/', views.login_view, name='login'),
    path('registrazione/', views.registrazione_view, name='registrazione'),
    path('logout/', views.logout_view, name='logout'),
    path('aggiungi_al_carrello/', views.aggiungi_al_carrello, name='aggiungi_al_carrello'),
    path('rimuovi-dal-carrello/<int:item_id>/', views.rimuovi_dal_carrello, name='rimuovi_dal_carrello'),
    path('pagamento/', views.pagina_pagamento_view, name='pagamento'),
    path('acquista_carrello/', views.acquista_carrello, name='acquista_carrello'),
    path('conferma_pagamento/', views.pagina_conferma_pagamento_view, name='conferma_pagamento'),
    path('lista_prodotti_cercati/', views.lista_prodotti_cercati_view, name='prodotti_cercati'),
    path('ordini/', views.lista_ordini, name='lista_ordini'),
    path('annulla_ordine/<int:ordine_id>/', views.annulla_ordine, name='annulla_ordine'),
    path('conferma_annullamento_ordine/', views.pagina_conferma_annullamento_view, name='pagina_annullamento'),

]



