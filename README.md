## Ohjelmistotekniikka

Kurssirepositorio aineopintojen kurssile Ohjelmistotekniikka **(5op)**

## PasswordManager App

Sovellus auttaa käyttäjää pitämään salasanansa muistissa ja turvassa. Sovelluksen avulla käyttäjä voi helposti kopioida pitkänkin salasanan clip-boardiin tai generoida uuden salasanan nappia painamalla. Sovellus perustuu siis käyttäjän eri sovellusten salasanojen hallinnointiin, eli salasanojen lisäys, poistaminen ja muuttaminen on kaikki mahdollista.

(HUOM, itse sovellus on kansiossa "pwmanager-app")

## Uusin lähdekoodi

[Release](https://github.com/oskari83/ot-harjoitustyo/releases/tag/Loppupalautus)

## Dokumentaatio

[Käyttöohje](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/dokumentaatio/testaus.md)

[Tuntikirjanpito](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/dokumentaatio/tuntikirjanpito.md)

[ChangeLog](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/dokumentaatio/changelog.md)

## Ohjelman Asennus

Siirry kansioon "pwmanager-app"

Asenna riippuvuudet komennolla:

```bash
poetry install
```

Alusta tietokanta komennolla:

```bash
poetry run invoke build
```

Ohjelma on valmis suoritettavaksi (ks. alla ohjeet)

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy käynnistämään komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti generoituu komennolla:

```bash
poetry run invoke coverage-report
```

### Linttaus

Linttauksen voi suorittaa komennolla:

```bash
poetry run invoke lint
```