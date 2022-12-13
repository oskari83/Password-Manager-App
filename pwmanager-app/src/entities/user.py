class User:
    """Käyttäjätunnusluokka, joka kuvaa yhtä käyttäjätunnusta muuttujilla 
    salasana ja käyttäjänimi.
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password
