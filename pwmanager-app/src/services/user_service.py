from entities.user import User
from entities.password import Password

from repositories.user_repository import (
    user_repository as default_user_repository
)

from repositories.password_repository import (
    password_repository as default_password_repository
)

class UserService:
    """Luokka, joka mahdollistaa käyttäjien luonnin, hallinnan, tunnistautumisen
    sekä yksittäisten salasanojen lisäämisen ja poiston.
    """

    def __init__(self):
        """Luokan konstruktori joka asettaa käyttäjä sekä salasana repositoriot sekä
        ylläpitää kirjautunutta käyttäjää muuttujissa.
        """

        self._user_repo = default_user_repository
        self._password_repo = default_password_repository
        self._logged_in = False
        self._current_user = None

    def create_account(self,username_input, password_input):
        """Luo uuden käyttäjätunnuksen sovellukseen.

        Args:
            username_input (merkkijono): annettu käyttäjänimi
            password_input (merkkijono): annettu salasana

        Returns:
            User: jos käyttäjänimi ei ole varattu, palauttaa User luokan instanssin
            luodusta käyttäjästä, muuten palauttaa None.
        """

        username_not_available = self._user_repo.find_user(username_input)
        if username_not_available:
            return None
        new_user = User(username_input,password_input)
        user = self._user_repo.insert_user(new_user)
        return user

    def authenticate(self, username, password_input):
        """Kirjaa käyttän sisään omalle tunnukselleen (tarkistaa että salasana ja
        käyttäjätunnus pari ovat oikein).

        Args:
            username (merkkijono): annettu käyttäjänimi
            password_input (merkkijono): annettu salasana

        Returns:
            User: palauttaa User luokan instanssin kirjautuneesta käyttäjätilistä,
            paitsi jos tunnukset eivät ole oikein, jolloin palauttaa None.
        """

        user_account = self._user_repo.find_user(username)
        if not user_account or user_account.password!=password_input:
            return None
        self._current_user = user_account
        return user_account

    def logout(self):
        """Kirjaa käyttäjän ulos sovelluksesta.
        """

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

        if not self._current_user:
            return None
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

        if not self._current_user:
            return None
        password_item = self._password_repo.find_password(app_input, self._current_user.username)
        if not password_item:
            return "Could not find such password item"
        self._password_repo.delete_password(password_item)
        return "Password entry deleted successfully"

    def get_all_user_passwords(self):
        """Hakee kaikki käyttäjän salasanat.

        Returns:
            lista: palauttaa listan Password luokan instansseja
        """

        password_list = self._password_repo.find_all(self._current_user.username)
        return password_list

    def get_current_user(self):
        """Hakee tällähetkellä sovellukseen kirjautuneen käyttäjän tiedot.

        Returns:
            User: palauttaa User luokan instanssin kirjautuneesta käyttäjästä
        """

        return self._current_user

user_service = UserService()
