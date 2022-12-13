# Arkkitehtuurikuvaus

## Rakenne

Ohjelman arkkitehtuurin rakenne on kolmitasoinen. Ylimpänä (eli käyttäjää lähesimpänä) on käyttöliittymästä vastaava pakkaus eli ui, keskellä on sovelluslogiikasta vastaava pakkaus services, ja alimpana tietokannan käsittelevä eli pysyväistallenuksesta huolehtiva repositories. Sovelluksen pakkausrakenne on visualisoitu alla olevassa kuvassa:

![alt text](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/pictures/rakenne.png?raw=true)

## Käyttöliittymä

Käyttöliittymä muodostuu kolmesta näkymästä. 

Ensimmäinen näkymä (`LoginView`) on sisäänkirjautumisesta huolehtiva näkymä, johon käyttäjä antaa käyttäjätunnuksen ja salasanan ja voi sen jälkeen painaa nappia kirjautuakseen sisään. Hän voi myös painaa nappia luodakseen käyttäjätunnuksen jos hänellä ei tätä vielä ole.

Toinen näkymä (`CreateAccountView`) on sisäänkirjautumisnäkymään liittyvä käyttäjän luomisen näkymä. Tässä käyttäjä voi antaa käyttäjänimen ja salasanan jolla luoda käyttäjätili, ja tähän liittyvä nappi. Näkymä sisältää myös tottakai napin sisäänkirjautumisnäkymään palaamiseen.

Kolmas päänäkymä (`PasswordsView`) on sovelluksen päänäkymä sillä sisäänkirjauduttuaan, käyttäjä näkee tässä näkymässä kaikki hänen tallentamat sovellusten salasanat listana. Näkymän ylälaidassa hän näkee myös oman käyttäjänimensä ja uloskirjautumisnapin. Alalaidassa hän voi antaa uuden sovelluksen nimen ja salasanan joka tallenetaan sovellukseen ja siihe liittyvän napin. 

Jokainen näkymä on oma luokkansa, joita hallitsee ylä-luokka `UI`, eli jonka vastuulla on näiden kolmen näkymän välillä vaihtaminen. Kaikki käyttöliittymän toiminnallisuus on eriytetty siten, että se kutsuu vain `UserService` luokan metodeja. 

## Sovelluslogiikka

Sovelluksen tietomalli perustuu kahteen luokkaan: `User` ja `Password`. `User` kuvaa käyttäjätunnusta ja sisältää käyttäjän käyttäjänimen ja salasanan merkkijonona. `Password` taas kuvaa käyttäjän tallentamaa salasananaa sisältämällä itse salasanan, salasanaan liittyvän sovelluksen nimen, ja käyttäjänimen käyttäjäst jolle se kuuluu merkkijonona.

Sovelluslogiikka perustuu `UserService` luokan metodeihin.
- Sisäänkirjautuminen tapahtuu `authenticate(username, password_input)` metodilla
- Salasanan lisääminen `add_password(app_input, password_input)` metodilla
- jne.

Eri luokkien ja pakkausten suhdetta kuvaava luokka/pakkauskaavio:

![alt text](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/pictures/new_architecture.png?raw=true)

## Tiedon tallennus

Sovellus tallentaa kaiken datan pysyvästi Sqlite tietokantaan. Tietokantaa käsittelevät `UserRepository` ja `PasswordRepository` jotka yhdessä tarjoavat `UserService` luokalle metodeja tallentamiseen/hakemiseen/poistamiseen.

## Toiminnallisuus

### Sisäänkirjautuminen

Käyttäjä voi kirjautua sisään sovellukseen kirjoittamalla merkkijonoja käyttäjänimeksi ja salasanaksi. Tämän jälkeen jos käyttäjä painaa nappia, kutsuu `UI` luokan hallitsema `LoginView` luokkaa annetuilla merkkijonoilla `UserService` luokan `authenticate(username,password_input)` metodia, joka taas kutsuu `UserRepository` luokkaa metodilla `find_user(username_input)` hakeakseen käyttäjänimeen liitetyn salasanan tietokannasta. `UserService` sitten vertaa näitä salasanoja keskenään, ja jos nämä ovat samat, tallettaa käyttäjän muuttujaan ja palauttaa `User` luokan instanssin käyttöliittymälle indikoiden että sisäänkirjautuminen onnistui. Tämän jälkeen `UI` luokka tietää vaihtaa näkymää `PasswordsView` luokan määritellemäksi eli päänäkymäksi.

Seuraava sekvenssidiagrammi havannoi toimintaa:

![alt text](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/pictures/login_sequence.png?raw=true)

### Salasanan lisääminen

Käyttäjä voi lisätä salasanan sovellukseen antamalla sovelluksen nimen ja salasanan merkkijonoina ja sitten painamalla Add-nappia käyttöliittymässä. Mahdollisesti käyttäjä voi myös autogeneroida salasanan painamalla ensin Generate-nappia. Tämän jälkeen kutsuu `UI` luokan hallitsema `PasswordsView` luokka `UserService` luokkaa metodilla `add_password(app_input, password_input)`, joka taas paketoi tiedon `Password` luokan instanssiin ja lähettää datan eteenpäin `PasswordRepository` luokalle metodilla `insert_password(password)`, joka vihdoin tallettaa salasanan tietokantaan. Tämän onnistumisesta indikoi sekä `PasswordRepository` ja `UserService` palauttamalla `Password` luokan instanssin takaisinpäin. `PasswordsView` sitten poistaa mahdollisen error-notifikaation ja uuddelleen renderöi listan salasanoja kutsumalla `_initialize_password_list()` funktiota. 

Seuraava sekvenssidiagrammi havannoi toimintaa:

![alt text](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/pictures/password_add.png?raw=true)

### Uloskirjautuminen

Käyttäjä voi kirjautua ulos painamalla Logout-nappia päänäkymässä, jonka jälkeen UI-luokan hallitsema `PasswordsView` luokka kutsuu `UserService` luokan `logout()` funktiota joka kirjaa käyttäjän ulos poistamalla käyttäjän tämänhetkisen käyttäjän muuttujasta. Tämän jälkeen `UI` luokka automaattisesti vaihtaa näkymää sisäänkirjautumisnäkymään kutsumalla `_show_login_view()` metodia. 

Seuraava sekvenssidiagrammi havannoi toimintaa:

![alt text](https://github.com/oskari83/ot-harjoitustyo/blob/master/pwmanager-app/pictures/logout_sequence.png?raw=true)