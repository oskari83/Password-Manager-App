from ui.login_view import LoginView
from ui.create_account_view import CreateAccountView
from ui.passwords_view import PasswordsView

class UI:
    """Pää-käyttöliittymäluokka joka hallinnoi kaikkia näkymiä ja vaihtelee niiden välillä.
    """
    def __init__(self, root):
        """Konstruktori, jolle annetaan ThemedTk instanssi

        Args:
            root (ThemedTk): annettu ThemedTk instanssi
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Sovelluksen avatessa avaa sisäänkirjautumisnäkymän.
        """
        self._show_login_view()

    def _hide_current_view(self):
        """Ottaa tämänhetkisen näkymän pois näkyvistä käyttöliittymässä.
        """
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        """Näyttää sisäänkirjautumisnäkymän.
        """
        self._hide_current_view()
        self._current_view = LoginView(
            self._root,
            self._show_passwords_view,
            self._show_create_account_view
        )
        self._current_view.pack()

    def _show_passwords_view(self):
        """Näyttää päänäkymän eli missä näkyy kaikki käyttäjän salasanat.
        """
        self._hide_current_view()
        self._current_view = PasswordsView(self._root, self._show_login_view)
        self._current_view.pack()

    def _show_create_account_view(self):
        """Näyttää käyttäjätunnuksen luontiin kuuluvan näkymän käyttöliittymässä.
        """
        self._hide_current_view()
        self._current_view = CreateAccountView(
            self._root,
            self._show_login_view,
            self._show_login_view
        )

        self._current_view.pack()
