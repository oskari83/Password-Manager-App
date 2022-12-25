# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus, eli Password Manager, auttaa käyttäjää pitämään salasanansa muistissa ja turvassa. Salasanat ovat turvassa, sillä sovellukseen kirjaudutaan omalla käyttäjätunnuksella ja tähän käyttäjätunnukseen liittyvä salasana eli ns. "master-password" encryptoidaan tietokantaan. Käyttäjän sovelluksiin liittyvät lisäämät salasanat pysyvät tallessa, sillä ne ovat tallennettuna tietokantaan. Lisäksi sovelluksen mahdollistaa nopean salasanojen kopioimisen ja luomisen.

## Käyttäjät

Sovelluksella on vain yhdenlaisia käyttäjiä, sillä tarvetta ylläpitäjälle tai erityisille rooleille ei ole. 

## Perusversion toiminnallisuudet

### Turvallisuus

- Aluksi mahdollisuus luoda käyttäjätili tai kirjautua sisään
- Klikatessa käyttäjätilin luontia pyytää sovellus käyttäjätunnuksen ja salasanan, ja luo sitten tilin, sekä samalla kirjaa käyttäjän sisään
- Sovellus tallentaa tämän ns. "master-passwordin" encryptattuna tietokantaan
- Sisäänkirjautuessa pyydetään käyttäjätunnusta ja salasanaa
  - jos yhdistelmä on oikea, pääsee käyttäjä sovelluksen pääkäyttöliittymään
  - jos yhdistelmä on väärä, ilmoittaa sovellus tästä eikä päästä käyttäjää kirjautumaan

### Tallennus

- Tallennetut salasanat ovat tietokannassa
- Päänäkymässä on lista käyttäjän eri sovelluksista joista hänellä on salasana tallessa
- Sovelluksen nimen vieressä on tähän liittyvä salasana
- Päänäkymässä on myös mahdollisuus lisätä uusi sovellus, joka pyytää sovelluksen nimen ja salasanan
- Päänäkymästä voi uloskirjautua
- Sovelluksen nimen vieressä on nappi salasanan vaihtamista varten
- Käyttäjä voi vaihtaa sovellukseen liittyvää salasanaa
- Samaan sovellukseen ei ole mahdollista vahingossa lisätä kahta salasanaa

### Käyttäjäkokemus

- sovellus toimii graafisella käyttöliittymällä
- Päänäkymässä sovellusten nimien vieressä on myös kopiointi nappi, joka kopio salasanan clip-boardiin
- Kun käyttäjä on lisäämässä uuden sovelluksen, pystyy hän autogeneroimaan salasanan sen sijaan että hän keksii itse

## Jatkokehitysideat

- Päänäkymässä sovellusten nimien vieressä olisi myös sovellukseen liittyvä sähköpostiosoite/käyttäjänimi
- Salasanoja ei näytettäisi heti, jotta esimerkiksi muut tietokoneen ympärillä olevat ihmiset eivät vahingossa näkisi niitä, vaan sovelluksessa olisi jokaisella salasanalle oma "show" nappi jos käyttäjä haluaa nähdä salasanan tekstimuodossa.
- Sovelluksesta voisi tehdä nettisovelluksen ja/tai tallentaa tietokannan pilveen jotta käyttäjä voisi tarkistaa eri salasanansa mistä tahansa laitteelta eli sovellus ei olisi ns. "device-dependent"