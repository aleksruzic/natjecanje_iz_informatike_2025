# SchoolApp

SchoolApp je web aplikacija razvijena u Django frameworku, namijenjena za upravljanje različitim aspektima školske administracije. Aplikacija omogućuje korisnicima prijavu kvarova, IT problema, unos podataka o ulasku u školu, podnošenje putnih naloga i drugo.


## Značajke

* **Upravljanje zahtjevima:** Korisnici mogu prijaviti kvarove i IT probleme, a administratori mogu pratiti i obrađivati te zahtjeve.
* **Kontrola ulaza:** Upravljanje evidencijom ulaska osoba u školu.
* **Putni nalozi:** Podnošenje i upravljanje putnim nalozima za zaposlenike.
* **Administracija korisnika i grupa:** Upravljanje korisničkim računima i dodjeljivanje uloga putem grupa.
* **Računovodstvo:** Upravljanje naknadama.
* **Paginacija:** Paginacija ispisa u svim listama.

## Tehnologije

* Django
* Python
* HTML
* CSS
* JavaScript
* SQLite Baza podataka

## Kako pokrenuti aplikaciju

1.  **Klonirajte repozitorij:**

    ```bash
    git clone [URL_REPOSITORIJA]
    cd SchoolApp
    ```

2.  **Kreirajte virtualno okruženje (preporučeno):**

    ```bash
    python -m venv venv
    source venv/bin/activate # Za Linux/macOS
    venv\Scripts\activate # Za Windows
    ```

3.  **Instalirajte ovisnosti:**

    ```
    u /SchoolAPP/settings.py, dodati ključ za enkripciju
    ```

4.  **Instalirajte ovisnosti:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Primijenite migracije:**

    opcionalno
     ```bash
    python manage.py makemigrations
    ```

    ```bash
    python manage.py migrate
    ```

6.  **Pokrenite razvojni poslužitelj:**

    ```bash
    python manage.py runserver
    ```

7.  **Kreirajte superusera:**

    ```bash
    python manage.py createsuperuser
    ```

8.  **Superuser:**

    Super user mora kreirate potrebne podatke (dodati škole i naknade u admin sučelju) za rad aplikacije i dodati role domaru, it adminima i računođama (nakon što se registriraju prvi put).

9.  **Otvorite aplikaciju u pregledniku:**

    Posjetite `http://127.0.0.1:8000/` u vašem web pregledniku.



## Korisnički vodič

* **Registracija:** Novi korisnici se mogu registrirati putem stranice `/register/`.
* **Prijava:** Registrirani korisnici se mogu prijaviti putem stranice `/login/`.
* **Odjava:** Prijavljeni korisnici se mogu odjaviti putem gumba `Logout`.
* **Zahtjevi:** Nakon prijave, korisnici mogu prijaviti kvarove i IT probleme putem stranica `/prijavi_kvar/` i `/prijavi_it_problem/`.
* **Kontrola ulaza:** Ovlašteni korisnici mogu unositi podatke o ulasku osoba u školu putem stranice `/kontrola_ulaz/`.
* **Putni nalozi:** Zaposlenici mogu podnositi putne naloge putem stranice `/putni_nalog/`.
* **Administracija:** Administratori mogu upravljati korisnicima, grupama, zahtjevima i putnim nalozima putem administratorskog sučelja `/admin/`.
