from entities.user import User
from services.password_service import password_service
from services.encryption_service import encryption_service

from repositories.user_repository import (
    user_repository as default_user_repository
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

        encrypted_user_password = encryption_service.encrypt_password(password_input)
        new_user = User(username_input, encrypted_user_password)
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
        if not user_account or encryption_service.password_match_comparison(password_input,user_account.password) == False:
            return None
        self._current_user = user_account
        password_service.set_user(user_account)
        return user_account

    def logout(self):
        """Kirjaa käyttäjän ulos sovelluksesta.
        """
        password_service.remove_user()
        self._current_user = None

    def get_current_user(self):
        """Hakee tällähetkellä sovellukseen kirjautuneen käyttäjän tiedot.

        Returns:
            User: palauttaa User luokan instanssin kirjautuneesta käyttäjästä
        """

        return self._current_user

    def get_logged_in_status(self):
        return self._logged_in

user_service = UserService()
