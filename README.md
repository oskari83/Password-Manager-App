## Ohjelmistotekniikka

Kurssirepositorio aineopintojen kurssile Ohjelmistotekniikka **(5op)**

## PasswordManager App

Sovellus auttaa käyttäjää pitämään salasanansa muistissa ja turvassa.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/dokumentaatio/tuntikirjanpito.md)

[ChangeLogi](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/dokumentaatio/changelog.md)

## Ohjelman Asennus

Asenna riippuvuudet komennolla:

```bash
poetry install
```

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

Testikattavuusraportin generoituu komennolla:

```bash
poetry run invoke coverage-report
```