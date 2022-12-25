# Testausdokumentti

Ohjelman testaus on suoritettu yksikkötestejä ja integraatiotestejä hyödyntäen UnitTest:iä käyttäen. Lisäksi järjestelmätasolla sovellusta on testattu manuaalisesti.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovellusloogiikasta vastaavia `UserService`, `PasswordService` sekä `EncryptionService` luokkia testataan [omilla](https://github.com/oskari83/ot-harjoitustyo/tree/master/pwmanager-app/src/tests) testiluokilla.
Testejä varten käytetään erityistä test_database.sqlite tietokantaa joka alustetaan sovelluksen yleisen alustuksen yhdeydessä `poetry run invoke build` komennolla. 

### Repositorio-luokat

Repositorioita eli `UserRepository` ja `PasswordRepository` luokkia testataan myös [yksikkötesteillä](https://github.com/oskari83/ot-harjoitustyo/tree/master/pwmanager-app/src/tests) sekä integraatiotesteinä implisiittisesti `UserService`, `PasswordService` sekä `EncryptionService` luokkien yksikkötesteissä. 

### Testauskattavuus

Kuten kuvassa ilmenee, UI:ta lukuunottamatta sovelluksen haarautumakattavuus on 96%

![](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/pictures/testauskuva.PNG?raw=true)

Sovelluksessa tiedostoja kuten main.py, initialize_database.py ja database_connection.py ei testattu koska ne eivät sinäänsä sisällä mitään sovellukselle ominaista logiikkaa ja ovat niin pieniä kooltaan, joten ne on jätetty haaraumakattavuudesta ulkopuolelle.

## Järjestelmätestaus

Järjestelmätestaus on sovelluksessa suoritettu täysin manuaalisesti kokeilemalla nappeja ja syöttämällä erilaisia inputteja tekstikenttiin.

### Asennus ja konfigurointi

Sovellusta on suoritettu ja testattu [käyttöohjeen](https://github.com/oskari83/ot-harjoitustyo/tree/master/pwmanager-app/dokumentaatio/kayttoohje.md) ohjeiden mukaisesti MacOS, Linux ja Windows (invoke/python3 komennot eivät toimi) ympäristöissä.

### Toiminnallisuudet

Kaikki [määrittelydokumentin](https://github.com/oskari83/ot-harjoitustyo/tree/master/pwmanager-app/dokumentaatio/vaatimusmäärittely.md) ja käyttöohjeessa selitetyt toiminnallisuudet on käyty lävitse. Kaikkien tekstikenttien kohdalla on kentät yritetty täyttää virheellisillä kuten tyhjillä arvoilla.

## Sovellukseen jääneet laatuongelmat

Sovellus ei tuo ilmi seuraavaa virhettä millään tavalla:

- SQLite tietokannan alustamatta jättäminen, eli `poetry run invoke build` komennon suorittamatta jättäminen