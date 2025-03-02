from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, LoginForm, PutniNalogForm
from django.contrib import messages
from django.urls import reverse
from .models import Zahtjev
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Ulaz, PutniNalog, Skola, UnosPutniNalog, Naknada
from django.db import transaction
from datetime import datetime
from django.shortcuts import get_object_or_404




def index(request):
    return render(request, "index.html")


# Pogled za registraciju korisnika
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Spremanje korisnika u bazu podataka
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Račun za {username} je uspješno kreiran!")
            # Preusmjerenje na stranicu za prijavu
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})



# Pogled za prijavu korisnika
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Pogrešno korisničko ime ili lozinka")
        else:
            messages.error(request, "Pogrešno korisničko ime ili lozinka")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


# Pogled za početnu stranicu
@login_required
def home(request):
    user = request.user
    first_name = user.first_name
    last_name = user.last_name
    return render(
        request, "home.html", {"first_name": first_name, "last_name": last_name}
    )


# Stranica za zahtjeve
@login_required
def zahtjevi(request):
    # Filtriraj zahtjeve samo za prijavljenog korisnika
    zahtjevi = Zahtjev.objects.filter(user=request.user)

    # Ako je zahtjev za brisanje, obriši ga
    if request.method == 'POST':
        zahtjev_id = request.POST.get('zahtjev_id')
        try:
            zahtjev = Zahtjev.objects.get(id=zahtjev_id, user=request.user)
            zahtjev.delete()
            messages.success(request, "Zahtjev je uspješno obrisan.")
        except Zahtjev.DoesNotExist:
            messages.error(request, "Zahtjev nije pronađen ili nemate pravo obrisati ga.")

    return render(request, "zahtjevi.html", {"zahtjevi": zahtjevi})


@login_required
def obrada_zahtjevi(request):
    # Prikaz svih zahtjeva za "domare", admine i superadmine
    if not (request.user.groups.filter(name='DOMAR').exists() or request.user.is_staff or request.user.is_superuser):
        # Preusmjeri korisnika na početnu ako nije "domar", admin ili superadmin
        return redirect('home')
    print("test")
    print(request.user.groups.values_list("name", flat=True))
    # Ako je korisnik "DOMAR", prikazi samo zahtjeve tipa KVAR, inače prikaži sve
    if request.user.groups.filter(name='DOMAR').exists():
        zahtjevi = Zahtjev.objects.filter(obraden_zahtjev=False, vrsta_zahtjeva="kvar")
        print(zahtjevi)
    else:
        zahtjevi = Zahtjev.objects.filter(obraden_zahtjev=False)
    return render(request, "obrada_zahtjevi.html", {"zahtjevi": zahtjevi})


@login_required
def svi_zahtjevi(request):
    # Prikaz svih zahtjeva za "domare", admine i superadmine
    if not (request.user.groups.filter(name='DOMAR').exists() or request.user.is_staff or request.user.is_superuser):
        # Preusmjeri korisnika ako nije "domar", admin ili superadmin
        return redirect('home')

    zahtjevi = Zahtjev.objects.all()
    return render(request, "svi_zahtjevi.html", {"zahtjevi": zahtjevi})


@login_required
def potvrda_obradi_zahtjev(request, zahtjev_id):
    zahtjev = get_object_or_404(Zahtjev, id=zahtjev_id)
    return render(request, 'potvrda_obradi_zahtjev.html', {'zahtjev': zahtjev})


@login_required
def confirm_obrada_zahtjeva(request, zahtjev_id):
    zahtjev = get_object_or_404(Zahtjev, id=zahtjev_id)
    
    # Postavljanje polja obraden_zahtjev na True
    zahtjev.obraden_zahtjev = True
    zahtjev.save()
    
    messages.success(request, "Zahtjev je uspješno obrađen!")
    
    return redirect('svi_zahtjevi')


@login_required
def prijavi_kvar(request):
    if request.method == "POST":
        naziv_zahtjeva = request.POST.get("naziv_zahtjeva")
        opis_zahtjeva = request.POST.get("opis_zahtjeva")

        try:
            # Spremi zahtjev u bazu podataka s korisnikom koji je prijavljen
            zahtjev = Zahtjev(
                naziv_zahtjeva=naziv_zahtjeva,
                opis_zahtjeva=opis_zahtjeva,
                user=request.user,
                vrsta_zahtjeva="kvar"
            )
            zahtjev.save()

            # TODO: Slanje email obavijesti administratoru
           
            # Dodaj poruku korisniku
            messages.success(request, "ZAHTJEV USPJEŠNO UNESEN")
            return redirect("zahtjevi")

        except Exception as e:
            # Ako dođe do greške, prikaži poruku
            messages.error(request, "GRESKA PRILIKOM UNOSA")
            return redirect("prijavi_kvar")

    return render(request, "prijavi_kvar.html")


@login_required
def prijavi_it_problem(request):
    if request.method == "POST":
        naziv_zahtjeva = request.POST.get("naziv_zahtjeva")
        opis_zahtjeva = request.POST.get("opis_zahtjeva")

        try:
            # Spremi zahtjev u bazu podataka s korisnikom koji je prijavljen
            zahtjev = Zahtjev(
                naziv_zahtjeva=naziv_zahtjeva,
                opis_zahtjeva=opis_zahtjeva,
                user=request.user,
                vrsta_zahtjeva="it_problem"
            )
            zahtjev.save()

            #TODO: Slanje email obavijesti administratoru
           
            # Dodaj poruku korisniku
            messages.success(request, "ZAHTJEV USPJEŠNO UNESEN")
            return redirect("zahtjevi")

        except Exception as e:
            # Ako dođe do greške, prikaži poruku
            print(e)
            messages.error(request, "GRESKA PRILIKOM UNOSA")
            return redirect("prijavi_it_problem")

    return render(request, "prijavi_it_problem.html")


@login_required
def kontrola_ulaz(request):
    if request.method == "POST":
        ime_osobe = request.POST.get("ime_osobe")
        prezime_osobe = request.POST.get("prezime_osobe")
        oib_osobe = request.POST.get("oib_osobe")
        razlog_dolaska = request.POST.get("razlog_dolaska")

        if ime_osobe and prezime_osobe and razlog_dolaska:
            Ulaz.objects.create(ime_osobe=ime_osobe, prezime_osobe=prezime_osobe, oib_osobe=oib_osobe, razlog_dolaska=razlog_dolaska, user=request.user)
            messages.success(request, "Osoba uspješno upisana!")
            return redirect("/home")
        else:
            messages.error(request, "Sva polja su obavezna!")

    return render(request, "kontrola_ulaz.html")

@transaction.atomic
@login_required
def putni_nalog(request):
    if request.method == 'POST':
        form = PutniNalogForm(request.POST)

        if form.is_valid():
            mjesec_str = form.cleaned_data['mjesec']
            mjesec_ispune = datetime.strptime(mjesec_str, '%Y-%m').date()

            skola_naziv = form.cleaned_data['skola']

            try:
                skola = Skola.objects.get(naziv=skola_naziv)
            except Skola.DoesNotExist:
                messages.error(request, f"Škola '{skola_naziv}' ne postoji.")
                return render(request, 'putni_nalog.html', {'form': form})

            putni_nalog = PutniNalog(
                mjesec_ispune=mjesec_ispune,
                skola=skola,
                user=request.user,
                obrazlozenje=form.cleaned_data['obrazlozenje']
            )
            # Spremimo putni_nalog najprije da dobijemo ID
            putni_nalog.save()

            for key, value in request.POST.items():
                if key.startswith('dolazak_'):
                    dan_broj = key.split('_')[1]
                    dan = dan_broj
                    dolazak = request.POST.get(f'dolazak_{dan_broj}')
                    odlazak = request.POST.get(f'odlazak_{dan_broj}')
                    prijevoz = request.POST.get(f'prijevoz_{dan_broj}')

                    # pretvorimo prazne stringove u None
                    dolazak = float(dolazak) if dolazak else None
                    odlazak = float(odlazak) if odlazak else None

                    if dan and (dolazak is not None or odlazak is not None or prijevoz):
                        unos = UnosPutniNalog(
                            putni_nalog=putni_nalog,
                            dan=dan,
                            dolazak_km=dolazak,
                            odlazak_km=odlazak,
                            prijevozno_sredstvo=prijevoz
                        )
                        unos.save()

            # Izračunamo ukupne kilometraže i naknade nakon što su spremljeni svi unosi
            putni_nalog = PutniNalog.objects.get(pk=putni_nalog.pk)
            ukupno_km = sum((unos.dolazak_km or 0) + (unos.odlazak_km or 0) for unos in putni_nalog.unosi.all())

            # Dohvatimo aktivnu naknadu po km
            aktivna_naknada = Naknada.objects.filter(aktivna_naknada=True).first()
            if aktivna_naknada:
                putni_nalog.naknada_po_km = aktivna_naknada.iznos
            else:
                putni_nalog.naknada_po_km = 0.16 # TODO dodati logika
                messages.warning(request, "Nema aktivne naknade po km. Postavljena je vrijednost .16")

            putni_nalog.ukupna_naknada = (putni_nalog.naknada_po_km or 1) * ukupno_km
            putni_nalog.save()

            messages.success(request, 'Putni nalog je uspješno podnesen.')
            return redirect('home')
        else:
            messages.error(request, 'Došlo je do pogreške u unosu.')
            return render(request, 'putni_nalog.html', {'form': form})

    else:
        form = PutniNalogForm()
        return render(request, 'putni_nalog.html', {'form': form})


@login_required
def odabir_putne_naknade(request, naknada_id):
    if not (request.user.groups.filter(name='RACUNOVODSTVO').exists() or request.user.is_staff or request.user.is_superuser):
        # Preusmjeri korisnika ako nije "domar", admin ili superadmin
        return redirect('home')
    # Potvrda odabira naknada
    sve_naknade = Naknada.objects.all()
    for n in sve_naknade:
        n.aktivna_naknada = False
    # Postavljanje polja odabrana na True
    naknada = get_object_or_404(Naknada, id=naknada_id)
    naknada.aktivna_naknada = True
    naknada.save()
    
    messages.success(request, "Zahtjev je uspješno obrađen!")
    
    return redirect('sve_putne_naknade')


@login_required
def sve_putne_naknade(request):
    # Prikaz svih zahtjeva za "domare", admine i superadmine
    if not (request.user.groups.filter(name='RACUNOVODSTVO').exists() or request.user.is_staff or request.user.is_superuser):
        # Preusmjeri korisnika ako nije "domar", admin ili superadmin
        return redirect('home')

    naknade = Naknada.objects.all()
    return render(request, "sve_putne_naknade.html", {"naknade": naknade})


@login_required
def lista_ulaza(request):
    # Dohvaćamo sve ulaze i sortiramo ih po ID-u (najnoviji prvi)
    ulazi = Ulaz.objects.all().order_by('-id')
    return render(request, 'lista_ulaza.html', {'ulazi': ulazi})
