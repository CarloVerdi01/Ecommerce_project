from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Prodotto, Taglia, Carrello, Ordine, DettaglioOrdine
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, Prefetch, Q
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
import logging, os
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from shutil import copyfile
from django.core.files import File
from django.conf import settings
from django.utils import timezone















def home_view(request):
    prodotti = Prodotto.objects.all()
    return render(request, 'home.html', {'prodotti':prodotti})



def lista_prodotti_uomo_view(request):
    """
    prodotti = Prodotto.objects.filter(Q(sesso="M") | (Q(sesso="UNISEX")))
    return render(request, 'lista_prodotti_uomo.html', {'prodotti': prodotti})
    """
    prodotti = Prodotto.objects.filter(Q(sesso="M") | Q(sesso="UNISEX"))

    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_uomo.html', {'prodotti': prodotti})

def lista_prodotti_donna_view(request):
    """
    prodotti = Prodotto.objects.filter(Q(sesso="F") | (Q(sesso="UNISEX")))
    return render(request, 'lista_prodotti_donna.html', {'prodotti': prodotti})
    """
    prodotti = Prodotto.objects.filter(Q(sesso="F") | Q(sesso="UNISEX"))

    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    # Passa i prodotti al template dopo aver aggiunto le somme delle quantità
    return render(request, 'lista_prodotti_donna.html', {'prodotti': prodotti})


def lista_prodotti_abbigliamento_view(request):
    """
    prodotti = Prodotto.objects.filter(categoria="ABBIGLIAMENTO")
    return render(request, 'lista_prodotti.html', {'prodotti':prodotti})
    """

    prodotti = Prodotto.objects.filter(categoria="ABBIGLIAMENTO")

    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti.html', {'prodotti': prodotti})


def lista_scarpe_view(request):
    """
    prodotti = Prodotto.objects.filter(categoria="SCARPE")
    return render(request, 'lista_prodotti.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(categoria="SCARPE")
    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti.html', {'prodotti': prodotti})

def lista_accessori_view(request):
    """
    prodotti = Prodotto.objects.filter(categoria="ACCESSORIO")
    return render(request, 'lista_prodotti.html', {'prodotti':prodotti})
    """

    prodotti = Prodotto.objects.filter(categoria="ACCESSORIO")
    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti.html', {'prodotti': prodotti})


def lista_profumi_view(request):
    """
    prodotti = Prodotto.objects.filter(categoria="PROFUMO")
    return render(request, 'lista_prodotti.html', {'prodotti':prodotti})
    """

    prodotti = Prodotto.objects.filter(categoria="PROFUMO")
    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti.html', {'prodotti': prodotti})


def lista_abbigliamento_uomo_view(request):
    """
    prodotti = Prodotto.objects.filter(Q(categoria='ABBIGLIAMENTO') & (Q(sesso='M') | Q(sesso='UNISEX')))
    return render(request, 'lista_prodotti_uomo.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(Q(categoria='ABBIGLIAMENTO') & (Q(sesso='M') | Q(sesso='UNISEX')))
    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_uomo.html', {'prodotti': prodotti})



def lista_maglie_uomo_view(request):
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='MAGLIA', sesso__in=['M', 'UNISEX'])
    return render(request, 'lista_prodotti_uomo.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='MAGLIA', sesso__in=['M', 'UNISEX'])
    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_uomo.html', {'prodotti': prodotti})



def lista_camicie_uomo_view(request):
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='CAMICIA', sesso__in=['M', 'UNISEX'])
    return render(request, 'lista_prodotti_uomo.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='CAMICIA', sesso__in=['M', 'UNISEX'])

    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_uomo.html', {'prodotti': prodotti})


def lista_felpe_uomo_view(request):
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='FELPA', sesso__in=['M', 'UNISEX'])
    return render(request, 'lista_prodotti_uomo.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='FELPA', sesso__in=['M', 'UNISEX'])
    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_uomo.html', {'prodotti': prodotti})


def lista_pantaloni_uomo_view(request):
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='PANTALONE', sesso__in=['M', 'UNISEX'])
    return render(request, 'lista_prodotti_uomo.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='PANTALONE', sesso__in=['M', 'UNISEX'])

    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_uomo.html', {'prodotti': prodotti})

def lista_giubbotti_uomo_view(request):
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='GIUBBOTTO', sesso__in=['M', 'UNISEX'])
    return render(request, 'lista_prodotti_uomo.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='GIUBBOTTO', sesso__in=['M', 'UNISEX'])
    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_uomo.html', {'prodotti': prodotti})


def lista_profumi_uomo_view(request):
    """
    prodotti = Prodotto.objects.filter(Q(categoria='PROFUMO') & (Q(sesso='M') | Q(sesso='UNISEX')))
    return render(request, 'lista_prodotti_uomo.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(Q(categoria='PROFUMO') & (Q(sesso='M') | Q(sesso='UNISEX')))
    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_uomo.html', {'prodotti': prodotti})



def lista_accessori_uomo_view(request):
    """
    prodotti = Prodotto.objects.filter(Q(categoria='ACCESSORIO') & (Q(sesso='M') | Q(sesso='UNISEX')))
    return render(request, 'lista_prodotti_uomo.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(Q(categoria='ACCESSORIO') & (Q(sesso='M') | Q(sesso='UNISEX')))

    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_uomo.html', {'prodotti': prodotti})


def lista_scarpe_uomo_view(request):
    """
    prodotti = Prodotto.objects.filter(Q(categoria='SCARPE') & (Q(sesso='M') | Q(sesso='UNISEX')))
    return render(request, 'lista_prodotti_uomo.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(Q(categoria='SCARPE') & (Q(sesso='M') | Q(sesso='UNISEX')))

    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_uomo.html', {'prodotti': prodotti})

def lista_abbigliamento_donna_view(request):
    """
    prodotti = Prodotto.objects.filter(Q(categoria='ABBIGLIAMENTO') & (Q(sesso='F') | Q(sesso='UNISEX')))
    return render(request, 'lista_prodotti_donna.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(Q(categoria='ABBIGLIAMENTO') & (Q(sesso='F') | Q(sesso='UNISEX')))
    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_donna.html', {'prodotti': prodotti})



def lista_maglie_donna_view(request):
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='MAGLIA', sesso__in=['F', 'UNISEX'])
    return render(request, 'lista_prodotti_donna.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='MAGLIA', sesso__in=['F', 'UNISEX'])

    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_donna.html', {'prodotti': prodotti})


def lista_camicie_donna_view(request):
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='CAMICIA', sesso__in=['F', 'UNISEX'])
    return render(request, 'lista_prodotti_donna.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='CAMICIA', sesso__in=['F', 'UNISEX'])
    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_donna.html', {'prodotti': prodotti})


def lista_felpe_donna_view(request):
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='FELPA', sesso__in=['F', 'UNISEX'])
    return render(request, 'lista_prodotti_donna.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='FELPA', sesso__in=['F', 'UNISEX'])

    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_donna.html', {'prodotti': prodotti})

def lista_pantaloni_donna_view(request):
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='PANTALONE', sesso__in=['F', 'UNISEX'])
    return render(request, 'lista_prodotti_donna.html', {'prodotti':prodotti})
    """

    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='PANTALONE', sesso__in=['F', 'UNISEX'])

    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_donna.html', {'prodotti': prodotti})


def lista_giubbotti_donna_view(request):
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='GIUBBOTTO', sesso__in=['F', 'UNISEX'])
    return render(request, 'lista_prodotti_donna.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(categoria='ABBIGLIAMENTO', tipo='GIUBBOTTO', sesso__in=['F', 'UNISEX'])

    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_donna.html', {'prodotti': prodotti})

def lista_profumi_donna_view(request):
    """
    prodotti = Prodotto.objects.filter(Q(categoria='PROFUMO') & (Q(sesso='F') | Q(sesso='UNISEX')))
    return render(request, 'lista_prodotti_donna.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(Q(categoria='PROFUMO') & (Q(sesso='F') | Q(sesso='UNISEX')))

    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_donna.html', {'prodotti': prodotti})

def lista_accessori_donna_view(request):
    """
    prodotti = Prodotto.objects.filter(Q(categoria='ACCESSORIO') & (Q(sesso='F') | Q(sesso='UNISEX')))
    return render(request, 'lista_prodotti_donna.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(Q(categoria='ACCESSORIO') & (Q(sesso='F') | Q(sesso='UNISEX')))

    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_donna.html', {'prodotti': prodotti})


def lista_scarpe_donna_view(request):
    """
    prodotti = Prodotto.objects.filter(Q(categoria='SCARPE') & (Q(sesso='F') | Q(sesso='UNISEX')))
    return render(request, 'lista_prodotti_donna.html', {'prodotti':prodotti})
    """
    prodotti = Prodotto.objects.filter(Q(categoria='SCARPE') & (Q(sesso='F') | Q(sesso='UNISEX')))

    for prodotto in prodotti:
        # Ottieni tutte le taglie associate al prodotto corrente
        taglie = Taglia.objects.filter(prodotto=prodotto)

        # Calcola la somma delle quantità delle taglie
        somma_quantita = taglie.aggregate(somma=Sum('quantità'))['somma']

        # Aggiungi la somma delle quantità come attributo al prodotto
        prodotto.somma_quantita_taglie = somma_quantita

    return render(request, 'lista_prodotti_donna.html', {'prodotti': prodotti})

def chi_siamo_view(request):
    return render(request, 'pagina_chi_siamo.html')

def termini_legali_e_privacy_view(request):
    return render(request, 'termini_legali_e_privacy.html')

def contatti_view(request):
    return render(request, 'contatti.html')

def cookie_view(request):
    return render(request, 'cookie.html')

def dettagli_prodotto_view(request, prodotto_id):
    prodotto = get_object_or_404(Prodotto, id=prodotto_id)
    taglie = Taglia.objects.filter(prodotto=prodotto)
    somma_quantità = sum([taglia.quantità for taglia in taglie])

    return render(request, 'schermata_prodotto.html', {'prodotto': prodotto, 'taglie': taglie, 'somma_quantità':somma_quantità})


def registrazione_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect alla home o alla pagina desiderata dopo la registrazione
    else:
        form = CustomUserCreationForm()  # Usa sempre il form personalizzato anche qui

    return render(request, 'registrazione.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect dove desideri dopo il login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('home')



def carrello_view(request):
    if request.user.is_authenticated:
        carrello_utente = Carrello.objects.filter(utente=request.user)
        totale_prezzi = sum(item.prezzo for item in carrello_utente)
        username = request.user.username

        context = {
            'carrello_utente': carrello_utente,
            'totale_prezzi': totale_prezzi,
            'username':username,
        }
        return render(request, 'carrello.html', context)
    else:
        return render(request, 'carrello.html')



@login_required
def rimuovi_dal_carrello(request, item_id):
    item = get_object_or_404(Carrello, id=item_id)

    if request.method == 'POST':
        item.delete()

    return redirect('carrello')  # Redirect alla pagina del carrello o altrove dopo la rimozione

@login_required
def aggiungi_al_carrello(request):
    if request.method == 'POST':
        prodotto_id = request.POST.get('prodotto_id')
        prodotto = Prodotto.objects.get(id=prodotto_id)

        utente = request.user

        taglia = None
        numero = None

        if prodotto.categoria == 'ABBIGLIAMENTO':
            taglia = request.POST.get('taglia')
        elif prodotto.categoria == 'SCARPE':
            numero = request.POST.get('numero')

        prezzo = request.POST.get('prezzo')
        quantita = request.POST.get('quantita')



        carrello_prodotto = Carrello.objects.create(
            utente=utente,
            prodotto=prodotto,
            taglia=taglia,
            numero=numero,
            prezzo=prezzo,
            quantita=quantita,
        )

        messages.success(request, 'Prodotto aggiunto al carrello!')

        return redirect('carrello')

    return redirect('pagina_dei_prodotti')




@login_required
def acquista_carrello(request):
    if request.method == 'POST':
        indirizzo_spedizione = request.POST.get('indirizzo_spedizione')
        metodo_pagamento = request.POST.get('metodo_pagamento')

        carrello_utente = Carrello.objects.filter(utente=request.user)

        totale_prezzi = sum(item.prezzo for item in carrello_utente)

        # Crea un nuovo oggetto Ordine
        nuovo_ordine = Ordine.objects.create(
            utente=request.user,
            data_ordine=timezone.now(),
            indirizzo_spedizione=indirizzo_spedizione,
            stato_ordine='IN_ATTESA',  # Puoi impostare uno stato predefinito se necessario
            metodo_pagamento=metodo_pagamento,
            numero_tracciamento='',  # Lascia vuoto inizialmente
            note_aggiuntive='',  # Lascia vuoto inizialmente
        )


        nuovo_ordine.save()

        for item in carrello_utente:
            DettaglioOrdine.objects.create(
                ordine=nuovo_ordine,
                prodotto=item.prodotto,
                quantita=item.quantita,
                prezzo=item.prezzo,
                taglia=item.taglia if item.prodotto.categoria == "ABBIGLIAMENTO" else None,
                numero=item.numero if item.prodotto.categoria == "SCARPE" else None
                # Aggiunge il numero solo se categoria è SCARPE

          )


        carrello_utente = Carrello.objects.filter(utente=request.user)

        taglia = None
        numero = None



        for item in carrello_utente:
            prodotto = item.prodotto
            taglia = item.taglia
            numero = item.numero
            quantita_da_decrementare = item.quantita

            if item.prodotto.categoria == "ABBIGLIAMENTO":
                taglia = item.taglia
                prodotto_abbigliamento = Taglia.objects.get(prodotto=item.prodotto, taglia=taglia)
                prodotto_abbigliamento.quantità -= item.quantita
                prodotto_abbigliamento.save()

            elif item.prodotto.categoria == "SCARPE":
                numero = item.numero
                prodotto_scarpe = Taglia.objects.get(prodotto=item.prodotto, numero=numero)
                prodotto_scarpe.quantità -= item.quantita
                prodotto_scarpe.save()

            else :
                prodotto_accessori = Taglia.objects.get(prodotto = prodotto)
                prodotto_accessori.quantità -= quantita_da_decrementare
                prodotto_accessori.save()



        carrello_utente.delete()

        return redirect('conferma_pagamento')
    else:

        return redirect('carrello')


@login_required
def pagina_pagamento_view(request):
        carrello_utente = Carrello.objects.filter(utente=request.user)
        totale_prezzi = sum(item.prezzo for item in carrello_utente)
        username = request.user.username

        context = {
            'carrello_utente': carrello_utente,
            'totale_prezzi': totale_prezzi,
            'username':username,
        }
        return render(request, 'pagina_pagamento.html', context)

@login_required
def pagina_conferma_pagamento_view(request):
    return render(request, 'conferma_acquisto.html')


def lista_prodotti_cercati_view(request):
    query = request.GET.get('q')
    if query:
        prodotti = Prodotto.objects.filter(nome__icontains=query)
    else:
        prodotti = Prodotto.objects.all()

    context = {
        'prodotti': prodotti,
        'query': query
    }

    return render(request, 'lista_prodotti.html', context)


@login_required
def lista_ordini(request):
    ordini = Ordine.objects.filter(utente=request.user).order_by('-data_ordine')
    context = {
        'ordini': ordini
    }
    return render(request, 'lista_ordini.html', context)


@login_required
def annulla_ordine(request, ordine_id):
    ordine = get_object_or_404(Ordine, id=ordine_id, utente=request.user)

    if request.method == 'POST':
        dettagli_ordine = DettaglioOrdine.objects.filter(ordine=ordine)

        for dettaglio in dettagli_ordine:
            if dettaglio.prodotto.categoria == "ABBIGLIAMENTO":
                taglia = dettaglio.taglia
                prodotto_abbigliamento = Taglia.objects.get(prodotto=dettaglio.prodotto, taglia=taglia)
                prodotto_abbigliamento.quantità += dettaglio.quantita  # Incrementa la quantità
                prodotto_abbigliamento.save()

            elif dettaglio.prodotto.categoria == "SCARPE":
                numero = dettaglio.numero
                prodotto_scarpe = Taglia.objects.get(prodotto=dettaglio.prodotto, numero=numero)
                prodotto_scarpe.quantità += dettaglio.quantita  # Incrementa la quantità
                prodotto_scarpe.save()

            else:
                prodotto_accessori = Taglia.objects.get(prodotto=dettaglio.prodotto)
                prodotto_accessori.quantità += dettaglio.quantita  # Incrementa la quantità
                prodotto_accessori.save()

        ordine.stato_ordine = 'ANNULLATO'
        ordine.save()

        return redirect('pagina_annullamento')  # Sostituisci con la tua URL di conferma


    context = {
        'ordine': ordine
    }
    return render(request, 'annulla_ordine.html', context)

@login_required
def pagina_conferma_annullamento_view(request):
    return render(request, 'pagina_annullamento.html')