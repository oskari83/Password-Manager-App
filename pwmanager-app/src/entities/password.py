class Password:
    """Luokka, jossa on tieto yksittäisestä salasanasta kuten itse salasana,
    sovelluksen nimi johon salasana liittyy, ja käyttäjänimi johon salasana
    liittyy.
    """

    def __init__(self, app, password, username):
        self.app = app
        self.password = password
        self.username = username
