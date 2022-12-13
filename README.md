## Ohjelmistotekniikka

Kurssirepositorio aineopintojen kurssile Ohjelmistotekniikka **(5op)**

## PasswordManager App

Sovellus auttaa käyttäjää pitämään salasanansa muistissa ja turvassa.

(HUOM, itse sovellus on kansiossa "pwmanager-app")

## Uusin lähdekoodi

[Release](https://github.com/oskari83/ot-harjoitustyo/releases/tag/viikko6)

## Dokumentaatio

[Käyttöohje](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/dokumentaatio/arkkitehtuuri.md)

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