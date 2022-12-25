from tkinter import ttk, constants, StringVar
from tkinter.font import BOLD, Font
from services.user_service import user_service

class CreateAccountView:
    """Luokka käyttäjätunnuksen luomiselle käyttöliittymässä.
    """

    def __init__(self, root, handle_create_account, handle_show_login_view):
        """Konstruktori, joka luo tarvittavat input-muuttujat (_username_input ja _password_input),
        tallettaa tarvittavat event handlerit nappien painalluksiin (_handle_create_account ja
        _handle_login_view), ja luo nappeihin ja teksteihin tarvittavat UI tyylit (_bold15 ja
        _error_font).

        Args:
            root (ThemedTK): ThemedTk pääinstanssi joka on luotu main.py Main metodissa
            handle_create_account (metodi): käyttäjätunnuksen luomisen napin painamisen event handleri
            handle_show_login_view (metodi): takaisin sisäänkirjautumisnäkymään napin painamisen event handleri
        """

        self._root = root
        self._handle_create_account = handle_create_account
        self._handle_show_login_view = handle_show_login_view

        self._frame = None
        self._username_input = None
        self._password_input = None

        self._error_variable = None
        self._error_label = None

        self._bold15 = Font(self._root, size=15, weight=BOLD)
        self._error_font = Font(self._root, size=8)

        self._initialize()

    def pack(self):
        """Näyttää elementit käyttöliittymässä"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Poistaa elementit käyttöliittymästä"""

        self._frame.destroy()

    def _show_error(self, message):
        """Näyttää virheilmoituksen annetulla tekstillä käyttöliittymässä"""

        self._error_variable.set(message)
        self._error_label.grid()
    
    def _hide_error(self):
        """Poistaa virheilmoituksen käyttöliittymästä"""

        self._error_label.grid_remove()
    
    def _create_account_handler(self):
        """Tarkistaa että käyttäjä on antanut jotain merkkejä käyttäjätunnukseksi
        ja salasanaksi ja välittää nämä sitten UserService:lle jotta käyttäjätunnus
        voidaan luoda näiden perusteella.
        """
        
        username = self._username_input.get()
        password = self._password_input.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error("Please input a username and password")
            return
        
        response = user_service.create_account(username,password)
        if response is not None:
            user_service.authenticate(username,password)
            self._handle_create_account()
        else:
            self._show_error("Username is already taken")
    
    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_input = ttk.Entry(master=self._frame)
        username_label.grid(padx=100, pady=(2,2),sticky=constants.W)
        self._username_input.grid(padx=100, pady=0,sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_input = ttk.Entry(master=self._frame, show="*")
        password_label.grid(padx=100, pady=(5,2),sticky=constants.W)
        self._password_input.grid(padx=100, pady=0,sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master = self._frame,
            textvariable=self._error_variable,
            font=self._error_font,
            foreground="red"
        )

        view_label = ttk.Label(master=self._frame, text="Create User Account", font=self._bold15)
        view_label.grid(padx=100, pady=(40,15),sticky=constants.W)

        self._initialize_username_field()
        self._initialize_password_field()

        create_account_button = ttk.Button(
            master = self._frame,
            text="Create Account",
            command=self._create_account_handler
        )

        login_button = ttk.Button(
            master = self._frame,
            text="Back to login",
            command=self._handle_show_login_view
        )

        self._frame.grid_columnconfigure(0,weight=1,minsize=400)
        create_account_button.grid(row=6, padx=100, pady=(10,2), sticky=constants.EW)
        login_button.grid(row=7, padx=100, pady=(4,50), sticky=constants.EW)

        self._error_label.grid(row=5, column=0, padx=100,pady=5, sticky=constants.EW)

        self._hide_error()
