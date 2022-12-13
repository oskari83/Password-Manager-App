# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus, eli Password Manager, auttaa käyttäjää pitämään salasanansa muistissa ja turvassa. Salasanat ovat turvassa, sillä sovellukseen kirjaudutaan omalla käyttäjätunnuksella. Salasanat taas pysyvät tallessa, sillä ne ovat tallennettuna tietokantaan. Lisäksi sovelluksen on tarkoitus mahdollistaa nopea salasanojen kopioiminen ja luominen niitä tarvittaessa.

## Käyttäjät

Sovelluksella on vain yhdenlaisia käyttäjiä, sillä tarvetta ylläpitäjälle tai erityisille rooleille ei ole. 

## Suunnitellut toiminnallisuudet

### Turvallisuus

- Aluksi mahdollisuus luoda käyttäjätili tai kirjautua sisään (TEHTY)
- Klikatessa käyttäjätilin luontia pyytää sovellus käyttäjätunnuksen ja salasanan, ja luo sitten tilin (TEHTY)
- Sisäänkirjautuessa pyydetään käyttäjätunnusta ja salasanaa (TEHTY)
  - jos yhdistelmä on oikea, pääsee käyttäjä sovelluksen pääkäyttöliittymään (TEHTY)
  - jos yhdistelmä on väärä, ilmoittaa sovellus tästä eikä päästä käyttäjää kirjautumaan (TEHTY)

### Tallennus

- Tallennetut salasanat ovat tietokannassa (TEHTY)
- Päänäkymässä on lista käyttäjän eri sovelluksista joista hänellä on salasana tallessa (TEHTY)
- Sovelluksen nimen vieressä on tähän liittyvä salasana (TEHTY)
- Päänäkymässä on myös mahdollisuus lisätä uusi sovellus, joka pyytää sovelluksen nimen ja salasanan (TEHTY)
- Päänäkymästä voi uloskirjautua (TEHTY)

### Käyttäjäkokemus

- sovellus toimii graafisella käyttöliittymällä (TEHTY)
- Päänäkymässä sovellusten nimien vieressä on myös kopiointi nappi, joka kopio salasanan clip-boardiin (TEHTY)
- Kun käyttäjä on lisäämässä uuden sovelluksen, pystyy hän autogeneroimaan salasanan sen sijaan että hän keksii itse (TEHTY)

## Jatkokehitysideat

- Sovelluksen nimen vieressä on nappi salasanan vaihtamista varten
- Päänäkymässä sovellusten nimien vieressä on myös sovellukseen liittyvä sähköpostiosoite/käyttäjänimi