"""
URL configuration for SchoolApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('lista_ulaza/', views.lista_ulaza, name='lista_ulaza'),
    # Ovo je početna stranica koja se otvara kad korisnik posjeti 127.0.0.1/
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    # Početna stranica nakon prijave
    path('home/', views.home, name='home'),
    # Stranica sa zahtjevima
    path('zahtjevi/', views.zahtjevi, name='zahtjevi'),
    path('prijavi_kvar/', views.prijavi_kvar, name='prijavi_kvar'),
    path('prijavi_it_problem/', views.prijavi_it_problem, name='prijavi_it_problem'),
    path('admin/', admin.site.urls),
    path('kontrola_ulaz/', views.kontrola_ulaz, name='kontrola_ulaz'),
    path('putni_nalog/', views.putni_nalog, name='putni_nalog'),
    path('obrada_zahtjevi/', views.obrada_zahtjevi, name='obrada_zahtjevi'),
    path('svi_zahtjevi/', views.svi_zahtjevi, name='svi_zahtjevi'),
    path('sve_putne_naknade/', views.sve_putne_naknade, name='sve_putne_naknade'),
    path('potvrda_obradi_zahtjev/<int:zahtjev_id>/', views.potvrda_obradi_zahtjev, name='potvrda_obradi_zahtjev'),
    path('confirm_obrada_zahtjeva/<int:zahtjev_id>/', views.confirm_obrada_zahtjeva, name='confirm_obrada_zahtjeva'),
    path('odaberi_naknadu/<int:naknada_id>/', views.odabir_putne_naknade, name='odaberi_naknadu'),
]
