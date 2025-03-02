from django.db import models
from django.contrib.auth.models import User
from encrypted_model_fields.fields import EncryptedCharField, EncryptedTextField, EncryptedIntegerField


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    adresa = EncryptedCharField(max_length=255, blank=True, null=True)
    grad = EncryptedCharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Zahtjev(models.Model):
    KVAR = "KVAR"
    IT_PROBLEM = "IT"
    VRSTA_CHOICES = [
        (KVAR, "Kvar"),
        (IT_PROBLEM, "IT Problem"),
    ]

    naziv_zahtjeva = models.CharField(max_length=255)
    opis_zahtjeva = EncryptedTextField()
    datum_zahtjeva = models.DateField(auto_now_add=True)
    obraden_zahtjev = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    vrsta_zahtjeva = models.CharField(max_length=20, choices=VRSTA_CHOICES, default=KVAR)

    def __str__(self):
        return f"{self.naziv_zahtjeva} ({self.get_vrsta_zahtjeva_display()})"


class Ulaz(models.Model):
    ime_osobe = EncryptedCharField(max_length=255)
    prezime_osobe = EncryptedCharField(max_length=255)
    oib_osobe = EncryptedCharField(max_length=255, unique=True, null=True)
    razlog_dolaska = EncryptedTextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.ime_osobe} {self.prezime_osobe} ({self.razlog_dolaska})"


class Skola(models.Model):
    naziv = models.CharField(max_length=255)
    adresa = models.CharField(max_length=255)

    def __str__(self):
        return self.naziv


class PutniNalog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skola = models.ForeignKey(Skola, on_delete=models.CASCADE, null=True)
    mjesec_ispune = models.DateField()
    datum_podnosenja = models.DateField(auto_now_add=True)
    naknada_po_km = models.FloatField(null=True) 
    ukupna_naknada = models.FloatField(null=True)
    zakljucan = models.BooleanField(default=False)
    obrazlozenje = EncryptedTextField(null=True)

    def set_naknada_po_km(self, value):
        self.naknada_po_km = value

    def get_naknada_po_km(self):
        return self.naknada_po_km

    def set_ukupna_naknada(self, value):
        self.ukupna_naknada = value

    def get_ukupna_naknada(self):
        return self.ukupna_naknada

    def __str__(self):
        return f"Putni nalog za {self.user.username} ({self.mjesec_ispune})"


class UnosPutniNalog(models.Model):
    putni_nalog = models.ForeignKey(PutniNalog, on_delete=models.CASCADE, related_name="unosi")
    dan = EncryptedIntegerField()
    dolazak_km = models.FloatField(default=0, null=True)
    odlazak_km = models.FloatField(default=0, null=True)
    prijevozno_sredstvo = EncryptedCharField(max_length=255, null=True)

    def set_dolazak_km(self, value):
        self.dolazak_km = value

    def get_dolazak_km(self):
        return self.dolazak_km

    def set_odlazak_km(self, value):
        self.odlazak_km = value

    def get_odlazak_km(self):
        return self.odlazak_km

    def __str__(self):
        return f"Unos za dan {self.dan} (Putni nalog: {self.putni_nalog})"


class Naknada(models.Model):
    iznos = models.FloatField(default=0)
    aktivna_naknada = models.BooleanField(default=False)

    def set_iznos(self, value):
        self.iznos = value

    def get_iznos(self):
        return self.iznos

    def save(self, *args, **kwargs):
        if self.aktivna_naknada:
            Naknada.objects.exclude(pk=self.pk).update(aktivna_naknada=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Naknada: {self.get_iznos()} EUR (Aktivna: {self.aktivna_naknada})"
