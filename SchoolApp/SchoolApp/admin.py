from django.contrib import admin
from .models import Skola, Naknada, Zahtjev

# Registriramo ove modele da bi se vidjeli u admin sučelju
admin.site.register(Skola)
admin.site.register(Naknada)
admin.site.register(Zahtjev)
