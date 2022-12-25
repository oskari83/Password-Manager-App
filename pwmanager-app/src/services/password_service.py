from entities.user import User
from entities.password import Password

from repositories.password_repository import (
    password_repository as default_password_repository
)

class PasswordService:
    """Luokka, joka mahdollistaa käyttäjien luonnin, hallinnan, tunnistautumisen
    sekä yksittäisten salasanojen lisäämisen ja poiston.
    """

    def __init__(self):
        """Luokan konstruktori joka asettaa käyttäjä sekä salasana repositoriot sekä
        ylläpitää kirjautunutta käyttäjää muuttujissa.
        """

        self._password_repo = default_password_repository
        self._logged_in = False
        self._current_user = None

    def add_password(self, app_input,password_input):
        """Lisää salasanan sovellukseen sillä hetkellä kirjautuneelle käyttäjälle.

        Args:
            app_input (merkkijono): annettu sovelluksen nimi
            password_input (merkkijono): annetun sovellukseen liittyvä salasana

        Returns:
            Password: palauttaa Password luokan instanssin luodusta salasanasta, paitsi
            jos sovellukseen ei ole kirjautunut kukaan käyttäjä, jolloin palauttaa None.
        """

        if not self._logged_in:
            return None
        password_item = self._password_repo.find_password(app_input, self._current_user.username)
        if password_item:
            return "App with that name already exists in the database"
        new_pass = Password(app_input,password_input,self._current_user.username)
        self._password_repo.insert_password(new_pass)
        return new_pass

    def delete_password(self, app_input):
        """Poistaa käyttäjän valitseman salasanan

        Args:
            app_input (merkkijono): annettu sovelluksen nimi johon liittyvä
            salasana halutaan poistaa

        Returns:
            merkkijono: Palauttaa statuksen siitä, että onnistuiko merkkijonon poistaminen, riippuen
            siitä, että löytyikö annetulla sovelluksen nimellä salasanaa.
        """

        if not self._logged_in:
            return None
        password_item = self._password_repo.find_password(app_input, self._current_user.username)
        if not password_item:
            return "Could not find such password item"
        self._password_repo.delete_password(password_item)
        return "Password entry deleted successfully"

    def change_password(self, password):
        if not self._logged_in:
            return None
        password_item = self._password_repo.find_password(password.app, self._current_user.username)
        if not password_item:
            return "Could not find such password item"
        self._password_repo.update_password(password)
        return password

    def get_all_user_passwords(self):
        """Hakee kaikki käyttäjän salasanat.

        Returns:
            lista: palauttaa listan Password luokan instansseja
        """
        if not self._logged_in:
            return None
        password_list = self._password_repo.find_all(self._current_user.username)
        return password_list

    def set_user(self, user:User):
        self._logged_in = True
        self._current_user = user

    def remove_user(self):
        self._logged_in = False
        self._current_user = None

password_service = PasswordService()