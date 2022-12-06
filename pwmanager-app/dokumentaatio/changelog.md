## Viikko 3

- Käyttäjä voi luoda tilin ja kirjautua sisään antamalla käyttäjänimen ja salasanan
- Lisätty User-luokka joka mallintaa käyttäjätiliä
- Lisätty UserDatabase-luokka joka toimii tietokannan hallintaluokkana, tässävaiheessa pitää datan vasta listassa
- Lisätty UserManager-luokka joka mahdollistaa uuden käyttäjätunnuksen luonnin sekä sisäänkirjautumisen
- Lisäksi lisätty consoleIO-luokka sekä PasswordManagerApp-luokka jotka yhdessä ovat vastuussa käyttöliittymästä, joka on tässävaiheessa vielä terminaali, mutta joka muutetaan visuaaliseksi myöhemmillä viikoilla
- Testattu, että UserManager-luokassa voi luoda käyttäjätunnuksen ja kirjautua sisään

## Viikko 4

- UserManager uudelleennimetty UserService luokaksi ja toiminnallisuus salasana/app kombinaation lisäämiseen, poistoon ja listaamiseen lisätty
- UserDatabase poistettu koska siitä tuli turha
- UserRepository luokka lisätty joka sisältää funktioita SQLite tietokannan lukemiseen ja tallentamiseen
- PasswordRepository luokka lisätty joka sisältää funktioita SQLite tietokannan lukemiseen ja tallentamiseen
- User luokka eriytetty omaan tiedostoon Entities kansioon
- Password luokka luotu joka sisältää salasanan luoman käyttäjätunnuksen, sovelluksen, sekä salasanan
- Database connection ja initialization tiedostot luotu jotka auttavat yhdistämään ja alustamaan/luomaan SQLite tietokannan
- PasswordManagerApp luokkaan lisätty uusi näkymä käyttäjälle ja status sisäänkirjautumisesta joka mahdollistaa käyttäjän kokemuksen eriyttämisen koti sekä kirjautumis-näkymiin
- Testi lisätty että samalla käyttäjänimellä ei voi tehdä kahta käyttäjätiliä
- Testi lisätty että väärällä salasanalla ei voi kirjautua
- Testi lisätty että UserRepository löytää kaikkien käyttäjien tiedot

## Viikko 5

- UI luokka luotu tkinter käyttöliittymää toteuttamaan
- LoginView ja CreateAccountView luokat luotu
- Visuaalinen käyttöliittymä toteutettu sisäänkirjautumiselle
- Visuaalinen käyttöliittymä toteutettu käyttäjän luomiselle
- UserService luokkaan toteutettu get_current_user ja logout metodit