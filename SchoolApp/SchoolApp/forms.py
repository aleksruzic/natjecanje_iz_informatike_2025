from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Skola

# Forma za registraciju korisnika (ime, prezime, username, lozinka)
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label='Ime')
    last_name = forms.CharField(max_length=100, required=True, label='Prezime')
    email = forms.EmailField(required=True, label='E-mail')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

# Forma za prijavu korisnika (username, lozinka)
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class PutniNalogForm(forms.Form):
    mjesec = forms.CharField(  # Promijenjeno na CharField
        label='Mjesec',
        widget=forms.DateInput(attrs={'type': 'month'})
    )
    skola = forms.ModelChoiceField(  # Promijenjeno na ModelChoiceField
            label='Škola',
            queryset=Skola.objects.all(),  # Dohvati sve škole iz baze
            empty_label="Odaberite školu",  # Opcija ako nema odabira
            widget=forms.Select(attrs={'class': 'form-control'})  # Dodaj klasu za stiliziranje
    )
    obrazlozenje = forms.CharField(
        label='Obrazloženje (opcionalno)',
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=False
    )
    # Polja za dnevne troškove (dinamički se generiraju u view-u)
    # Ovdje ih ne definiramo jer se ponavljaju za svaki dan
