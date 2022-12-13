# Käyttöohje

Lataa viimeisin lähdekoodi uusimmasta [release](https://github.com/oskari83/ot-harjoitustyo/releases):sta valitsemalla Assets-osion alta Source code zip muodossta ja unzip:paa paketti tietokoneellasi.

## Ohjelman valmistelu/konfigurointi/alustaminen

Ohjelma täytyy ensin valmistella ja alustaa jotta sen voi suorittaa.

Asenna ensin riippuvuudet suorittamalla:

```
poetry install
```

Alusta sitten tietokanta suorittamalla:

```
poetry run invoke build
```

## Ohjelman käynnistäminen

Ohjelman konfiguroinnin ja alustamisen jälkeen olemme valmiita käynnistämään ohjelman. Tämä tapahtuu suorittamalla seuraavan komennon:

```
poetry run invoke start
```

## Sisäänkirjautuminen

Sovellus näyttää käynnistyksen jälkeen seuraavalta:
![alt text](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/pictures/ohje1.png?raw=true)

Sovellukseen täytyy ensin luoda käyttäjätunnus painamalla "Create Account"-nappia.

Tämän jälkeen sovellus näyttää seuraavalta:
![alt text](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/pictures/ohje2.png?raw=true)

Tämän jälkeen täytyy kirjoittaa käyttäjänimi ja salasana ja painaa "Create Account"-nappia. Jos sovellus sanoo käyttäjänimen olevan jo varattuna, muuta käyttäjänimeäsi kirjoittamalla jokin muu käyttäjänimi ja painamalla "Create Account"-nappia uudelleen.

Tämän jälkeen sovellus vie takaisin sisäänkirjautumisnäkymään, johon voit uudelleen kirjoittaa äsken luomasi tunnuksesi ja painamalla "Login"-nappia, kuten näkyy:
![alt text](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/pictures/ohje3.png?raw=true)

## Salasanan lisäys

Voit tallettaa salasanan sovellukseen kirjoittamalla siihen liittyvän sovelluksen nimen ja itse salasanan ruudun alalaidassa näkyviin laatikkoihin, ja painamalla "Add"-nappia, kuten näkyy:
![alt text](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/pictures/ohje4.png?raw=true)

Voit myös mahdollisesti autogeneroida uuden salasanan painamalla "Generate"-nappia.

## Salasanan poistaminen/kopioiminen

Voit poistaa tai kopioida salasanan clip-boardiisi painamalla joko "Delete" tai "Copy"-nappia salasanan oikealla puolella kuten näkyy:
![alt text](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/pictures/ohje5.png?raw=true)

## Uloskirjautuminen

Voit kirjautua ulos painamalla sovelluksen päänäkymässä oikeassa ylälaidassa näkyvää "logout"-nappia. Tämän jälkeen olet kirjautunut ulos.
