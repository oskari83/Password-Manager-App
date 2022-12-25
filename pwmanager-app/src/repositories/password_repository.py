from database_connection import get_database_connection
from entities.password import Password

def get_password_by_row(row):
    """Luo Password luokan instanssin annetusta Dictionary tietorakenteesta.

    Args:
        row (dictionary): dictionary joka sisältää tietokannasta haetun rivin datan.

    Returns:
        Password: Palauttaa Password luokan instanssin tietokannasta haetun datan perusteella,
        paitsi jos dictionary data on annettu, muuten palauttaa None.
    """

    return Password(row["app"], row["password"], row["username"]) if row else None


class PasswordRepository:
    """Luokka, joka käsittelee SQLite tietokantaa ja mahdollistaa tiedon
    hakemisen ja lisäämisen sinne. Tässä tapauksessa se hallitsee Salasanojen
    tallentamista, lukemista ja poistamista.
    """

    def __init__(self, connection):
        """Konstruktori, joka laittaa annetun tietokantayhteyden muuttujaan

        Args:
            connection (Connection): Sqlite connection instanssi
        """

        self._connection = connection

    def find_all(self, username):
        """Hakee kaikki käyttäjätunnukseen liitetyt salasanat (eli kaikki annetun käyttäjän
        tallennetut salasanat) tietokannasta.

        Args:
            username (merkkijono): käyttätunnuksen käyttäjänimi

        Returns:
            lista: palauttaa listan Password luokan instansseja jotka kuuluvat annetulle
            käyttäjänimelle.
        """
        cursor = self._connection.cursor()
        sql = "SELECT * FROM passwords WHERE username=?"
        cursor.execute(sql,(username,))
        rows = cursor.fetchall()
        return list(map(get_password_by_row,rows))

    def delete_all(self):
        """Poistaa kaikki salasanat tietokannasta (Vain tietokannan alustamiseen, ei sovelluksen
        käyttämiseen tarkoitettu).
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM passwords")
        self._connection.commit()
        print('Deleted', cursor.rowcount, 'records from the table')

    def find_password(self, app_name, username):
        """Etsii käyttäjän tietyn sovellukseen liittyvän salasanan tietokannasta.

        Args:
            app_name (merkkijono): annetun sovelluksen nimi johon liittyvä salasana halutaan etsiä
            username (merkkijono): annettu käyttäjänimi jonka salasanoja etsitään

        Returns:
            Password: Palauttaa Password luokan instanssin jos sovelluksen nimeen ja käyttäjänimeen
            löytyy salasana tietokanasta, muuten palauttaaa None.
        """
        cursor = self._connection.cursor()
        sql = "SELECT * FROM passwords WHERE username=? AND app=?"
        cursor.execute(sql, (username,app_name))
        rows = cursor.fetchall()
        if len(rows) == 0:
            return None
        return get_password_by_row(rows[0])

    def insert_password(self, password):
        """Lisää (tallettaa) tietokantaan salasanan.

        Args:
            password (Password): annettu Password luokan instanssi jossa on tarvittava data

        Returns:
            Password: Palauttaa tallennetun salasanan Password luokan instanssin.
        """
        cursor = self._connection.cursor()
        sql = "INSERT INTO passwords (username,app,password) VALUES (?,?,?)"
        cursor.execute(sql, (password.username, password.app, password.password))
        self._connection.commit()
        return password

    def delete_password(self, password):
        """Poistaa salasanan tietokannasta.

        Args:
            password (Password): annetun salasanan Password luokan instanssi, joka halutaan poistaa

        Returns:
            Password: palauttaa poistetun salasanan Password luokan instanssin.
        """
        cursor = self._connection.cursor()
        sql = "DELETE FROM passwords WHERE username=? AND app=?"
        cursor.execute(sql, (password.username, password.app))
        self._connection.commit()
        return password

    def update_password(self, password):
        cursor = self._connection.cursor()
        sql = "UPDATE passwords SET password = ? WHERE username=? AND app=?"
        cursor.execute(sql, (password.password, password.username, password.app))
        self._connection.commit()
        return password

password_repository = PasswordRepository(get_database_connection())
