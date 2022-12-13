from database_connection import get_database_connection
from entities.user import User

def get_user_by_row(row):
    """Luo User luokan instanssin annetusta Dictionary tietorakenteesta.

    Args:
        row (dictionary): dictionary joka sisältää tietokannasta haetun rivin datan.

    Returns:
        User: Palauttaa User luokan instanssin tietokannasta haetun datan perusteella,
        paitsi jos dictionary data on annettu, muuten palauttaa None.
    """
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    """Luokka, joka käsittelee SQLite tietokantaa ja mahdollistaa tiedon hakemisen ja lisäämisen sinne.
    Tässä tapauksessa se hallitsee käyttäjien tallentamista, lukemista ja poistamista.
    """
    def __init__(self, connection):
        """Konstruktori, joka laittaa annetun tietokantayhteyden muuttujaan

        Args:
            connection (Connection): Sqlite connection instanssi
        """
        self._connection = connection

    def find_all(self):
        """Hakee kaikki käyttäjätunnukset tietokannasta.

        Returns:
            lista: palauttaa listan User luokan instansseja tietokannasta haetun datan perusteella. 
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return list(map(get_user_by_row,rows))

    def delete_all(self):
        """Poistaa kaikki käyttäjät tietokannasta (Vain tietokannan alustamiseen, ei sovelluksen
        käyttämiseen tarkoitettu).
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()

    def insert_user(self, user):
        """Lisää (tallettaa) tietokantaan käyttäjätunnuksen eli sen tiedot.
 
        Args:
            user (User): annettu User luokan instanssi jossa on tarvittava data

        Returns:
            User: Palauttaa tallennetun käyttäjän User luokan instanssin.
        """
        cursor = self._connection.cursor()
        sql = "INSERT INTO users (username,password) VALUES (?,?)"
        cursor.execute(sql, (user.username,user.password))
        self._connection.commit()
        return user

    def find_user(self, username):
        """Etsii käyttäjätunnuksen (eli käyttäjän tiedot) tietokannasta

        Args:
            username (merkkijono): annettu käyttäjänimi jonka tietoja etsitään

        Returns:
            User: Palauttaa User luokan instanssin jos käyttäjänimeen
            löytyy käyttäjä tietokannasta, muuten palauttaaa None.
        """
        cursor = self._connection.cursor()
        sql = "SELECT * FROM users WHERE username=?"
        cursor.execute(sql, (username,))
        rows = cursor.fetchall()
        if len(rows)>=1:
            return get_user_by_row(rows[0])
        return None

user_repository = UserRepository(get_database_connection())
    