## TODO Funkcionalnosti

### Zahtjevi

* **MOJI ZAHTJEVI:**
    * Maknuti gumb OBRISI sa obrađenih zahtjeva
    * Dodati filter/gumb za prikaz ZAKLJUČANIH (obrađenih) zahtjeva (korisnička strana).
    * Na refresh se prikazuje error da Zahtjev nije obrisan

* **SVI ZAHTJEVI:**
    * Maknuti gumb OBRISI sa obrađenih zahtjeva
    * Dodati filter/gumb za prikaz ZAKLJUČANIH (obrađenih) zahtjeva (korisnička strana). - odluceno da ce se makn

### Putni nalog

* **PUTNI NALOG:**
    * Nakon uspješnog unosa, preusmjeriti na stranicu "Moji nalozi". ✔️ NAPRAVLJENO
    * **OBAVEZNO:** Dodati stranicu "MOJI PUTNI NALOZI" s listom putnih naloga. Klikom na nalog, otvara se detaljan prikaz (s mogućnošću izmjene).
    * Prikaz obrazloženja samo ako postoje 2 ista dana u putnom nalogu.
    * Dodati mogućnost unosa PUTNOG NALOGA za određeni dan (npr. 1. i 15. u mjesecu).
    * Dodati padajuci izbornik za Skole - ✔️ NAPRAVLJENO

### Login / Registracija

* **LOGIN:**
    * Dodati provjeru jedinstvenosti e-mail adrese prilikom registracije.

* **LOGOUT:**
    * Dodati logout (koji vodi na login) ✔️ NAPRAVLJENO 17.02.

### Korisnici / Grupe

* **GRUPE:**
    * Dodati grupu "Domar" (dodano kao superuser) - ✔️ NAPRAVLJENO
    * Grupa "Domar" mora vidjeti predane zahtjeve (kvarove) - ✔️ NAPRAVLJENO.
    * Dodati grupu "Računovođa" (dodati kao superuser).  ✔️ NAPRAVLJENO
    * "Računovođa" mora vidjeti predane putne naloge.
    * Grupa "Admin" mora vidjeti sve zahtjeve/naloge. ✔️ NAPRAVLJENO
    * Razmotriti dodavanje ostalih grupa (ravnatelj / IT itd.).

### Računovodstvo

* Dodati gumb "Dodaj naknadu" za administriranje naknada. ✔️ NAPRAVLJENO

## Sređivanje Koda (Refaktoriranje)

* **KONVENCIJE:**
    * Ujednačiti naming konvencije (hrvatski ili engleski naziv funkcija, varijabli, klasa itd).
* **STRUKTURA:**
    * Razdvojiti prevelike funkcije.
    * Razmotriti razbijanje `views.py` u više datoteka.
    * Pojednostaviti HTML strukturu.
    * Obrisati nekorišteni kod i mape. ✔️ NAPRAVLJENO
* **KOMENTARI:**
    * Premjestiti komentare iznad koda. ✔️ NAPRAVLJENO
* **IMENOVANJE:**
    * Poboljšati imena funkcija i klasa (npr. `ULAZ` model).
* **CSS/HTML:**
    * Srediti CSS/HTML strukturu za "Putni nalog".  ✔️ NAPRAVLJENO
* **PAGINACIJA:**
    * Dodati paginaciju ispisa u svim listama.

## Dokumentacija

* **TEHNIČKA DOKUMENTACIJA:**
    * Napisati tehničku dokumentaciju. ✔️ NAPRAVLJENO
* **README.md:**
    * Napisati upute za pokretanje aplikacije i kratki korisnički vodič. ✔️ NAPRAVLJENO
