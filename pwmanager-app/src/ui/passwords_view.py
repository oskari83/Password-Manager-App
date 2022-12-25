from tkinter import ttk, constants, StringVar
from tkinter.font import BOLD, Font
from services.user_service import user_service
from services.password_service import password_service
from entities.password import Password
import random, string

class PasswordListView:
    """Luokka joka listaa salasanat käyttäjän eri sovelluksiin ja
    mahdollistaa poistamisen/kopioimisen
    """

    def __init__(self, master_root, root, passwords, handle_delete_password, handle_edit_password, handle_cancel_edit_password, handle_update_password, app_modes):
        self._master_root = master_root
        self._root = root
        self._passwords = passwords
        self._handle_delete_password = handle_delete_password
        self._handle_edit_password = handle_edit_password
        self._handle_cancel_edit_password = handle_cancel_edit_password
        self._handle_update_password = handle_update_password
        self._frame = None
        self._app_modes = app_modes

        self._initialize()

    def pack(self):
        """Näyttää elementit käyttöliittymässä"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Poistaa elementit käyttöliittymästä"""
        
        self._frame.destroy()

    def _copy_to_clipboard_handler(self, text):
        """Kopioi kyseiseen sovellukseen liittyvän salasanan käyttäjän tietokoneen
        clip-boardiin eli käyttäjä voi paste:ttaa sen CTRL+V käyttäen sovelluksen 
        ulkopuolella.

        Args:
            text (merkkijono): annettu salasana joka asetetaan clip-boardiin
        """

        self._master_root.clipboard_clear()
        self._master_root.clipboard_append(text)
        self._master_root.update()

    def _initialize_password_item(self, password, mode):
        item_frame = ttk.Frame(master=self._frame)
        labelApp = ttk.Label(master=item_frame,text=f"{password.app}:")

        if mode==0:
            labelPassword = ttk.Label(master=item_frame,text=password.password)

            copy_to_clipboard_button = ttk.Button(master=item_frame,text="Copy",command=lambda: self._copy_to_clipboard_handler(password.password))
            edit_password_button = ttk.Button(master=item_frame,text="Edit",command=lambda: self._handle_edit_password(password.app))

            copy_to_clipboard_button.grid(row=0,column=2,padx=(5,5),pady=5,sticky=constants.EW)
            edit_password_button.grid(row=0,column=3,padx=(5,100),pady=5,sticky=constants.EW)

            labelPassword.grid(row=0,column=1,padx=(5,5),pady=5,sticky=constants.EW)
        else:
            edit_password_input = ttk.Entry(master=item_frame)

            delete_password_button = ttk.Button(master=item_frame,text="Delete",command=lambda: self._handle_delete_password(password.app))
            save_edit_button = ttk.Button(master=item_frame,text="Save",command=lambda: self._handle_update_password(Password(password.app,edit_password_input.get(),password.username)))
            cancel_edit_button = ttk.Button(master=item_frame,text="Cancel",command=lambda: self._handle_cancel_edit_password(password.app))
            
            delete_password_button.grid(row=0,column=2,padx=(5,5),pady=5,sticky=constants.EW)
            save_edit_button.grid(row=0,column=3,padx=(5,5),pady=5,sticky=constants.EW)
            cancel_edit_button.grid(row=0,column=4,padx=(5,100),pady=5,sticky=constants.EW)

            edit_password_input.grid(row=0,column=1,padx=(5,5),pady=5,sticky=constants.EW)

            edit_password_input.delete(0, constants.END)
            edit_password_input.insert(0, password.password)

        labelApp.grid(row=0,column=0,padx=(100,5),pady=5,sticky=constants.EW)

        item_frame.grid_columnconfigure(0,weight=0,minsize=100)
        item_frame.grid_columnconfigure(1,weight=1,minsize=200)
        item_frame.grid_columnconfigure(2,weight=0)
        item_frame.grid_columnconfigure(3,weight=0)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        
        for pw in self._passwords:
            self._initialize_password_item(pw, self._app_modes[pw.app])

class PasswordsView:
    """Luokka joka on sovelluksen päänäkymä eli pitää sisällään uloskirjautumis napin,
    listan käyttäjän salasanoista, ja alhaalla mahdollisuuden lisätä uusi salasana.
    """

    def __init__(self, root, handle_logout):
        """Konstruktori, joka luo tarvittavat input-muuttujat (_create_password_input_password 
        ja _create_password_input_app), tallettaa UserService luokan referenssin muuttujaan,
        ja luo nappeihin ja teksteihin tarvittavat UI tyylit (_bold10 ja _error_font).

        Args:
            root (ThemedTK): ThemedTk pääinstanssi joka on luotu main.py Main metodissa
            handle_logout (metodi): käyttäjän uloskirjautumisen napin painamisen event handleri
        """

        self._root = root
        self._handle_logout = handle_logout
        self._user = user_service.get_current_user()
        self._frame = None
        # mode=0 tarkoittaa että olemme normaalinäkymässä, mode=1 tarkoittaa että olemme edit-näkymässä
        self._app_edit_mode = {}

        self._create_password_input_password = None
        self._create_password_input_app = None

        self._password_list_frame = None
        self._password_list_view = None

        self._error_variable = None
        self._error_label = None

        self._error_font = Font(self._root, size=8)
        self._bold10 = Font(self._root, size=10, weight=BOLD)

        self._initialize()

    def pack(self):
        """Näyttää elementit käyttöliittymässä"""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Poistaa elementit käyttöliittymästä"""

        self._frame.destroy()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()
    
    def _hide_error(self):
        self._error_label.grid_remove()

    def _logout_handler(self):
        """Kirjaa käyttäjän ulos sovelluksesta välittämällä pyynnön
        UserService luokalle. 
        """

        user_service.logout()
        self._handle_logout()

    def _handle_edit_password(self, password_app):
        self._app_edit_mode[password_app] = 1
        self._initialize_password_list()

    def _handle_cancel_edit_password(self, password_app):
        self._app_edit_mode[password_app] = 0
        self._initialize_password_list()

    def _handle_update_password(self, password):
        if len(password.password) == 0:
            self._show_error(f"Error, cannot update password. Empty password for App: {password.app} .")
            return
        self._hide_error()
        self._app_edit_mode[password.app] = 0
        password_service.change_password(password)
        self._initialize_password_list()

    def _handle_delete_password(self, password_app):
        """Välittää sovelluksen nimen UserServicelle johon liittyvä
        salasana halutaan poistaa.

        Args:
            password_app (merkkijono): sovellus jonka salasana halutaan poistaa
        """

        password_service.delete_password(password_app)
        self._initialize_password_list()

    def _initialize_password_list(self):
        if self._password_list_view:
            self._password_list_view.destroy()

        passwords = password_service.get_all_user_passwords()
        for password in passwords:
            self._app_edit_mode[password.app] = self._app_edit_mode.get(password.app, 0)

        self._password_list_view = PasswordListView(
            self._root,
            self._password_list_frame,
            passwords,
            self._handle_delete_password,
            self._handle_edit_password,
            self._handle_cancel_edit_password,
            self._handle_update_password,
            self._app_edit_mode
        )

        self._password_list_view.pack()

    def _initialize_header(self):
        """Luo tekstin joka kertoo kirjautuneen käyttäjän käyttäjänimen ja uloskirjautumiseen napin
        päänäkymän yläreunaan.
        """

        user_label = ttk.Label(master=self._frame, text=f"Logged in:    {self._user.username}", font=self._bold10)
        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command = self._logout_handler
        )

        header_label = ttk.Label(master=self._frame, text="Passwords (App: Password)", font=self._bold10)

        user_label.grid(row=0,column=0,padx=(100,5),pady=(40,5),sticky=constants.W)
        logout_button.grid(row=0, column=3, padx=(5,100),pady=(40,5),sticky=constants.EW)
        header_label.grid(row=1,column=0,padx=(100,5),pady=(15,5),sticky=constants.W)
    
    def _handle_create_password(self):
        """Tarkistaa että käyttäjä on kirjoittanut jotain merkkejä salasanan sovelluksen
        nimeksi ja itse salasanaksi ja välittää nämä merkkijonot sitten UserServicelle
        jotta ne voidaan tallentaa sovellukseen.
        """

        password_item_password = self._create_password_input_password.get()
        password_item_app = self._create_password_input_app.get()

        if len(password_item_password) == 0 or len(password_item_app) == 0:
            self._show_error("Empty app name or password")
            return

        if password_item_password and password_item_app:
            response = password_service.add_password(password_item_app,password_item_password)
            if isinstance(response, str):
                self._show_error(response)
            else:
                self._hide_error()
                self._initialize_password_list()
                self._create_password_input_password.delete(0,constants.END)
                self._create_password_input_app.delete(0,constants.END)

    def _handle_generate_password(self):
        """Generoi satunnaisen 16-merkin salasanan isoista ja pienistä aakkosista ja numeroista,
        ja näyttää tämän salasanan sitten käyttöliittymässä.
        """

        generated_password = "".join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) for _ in range(16))
        self._create_password_input_password.delete(0, constants.END)
        self._create_password_input_password.insert(0, generated_password)

    def _initialize_footer(self):
        """Luo input-boksit sovelluksen nimelle, salasanalle ja napit salasanan
        autogeneroimiseen ja tallentamiseen sovelluksen päänäkymän alareunaan.
        """

        self._create_password_input_app = ttk.Entry(master=self._frame)
        self._create_password_input_password = ttk.Entry(master=self._frame)

        autogenerate_password_button = ttk.Button(
            master=self._frame,
            text="Generate",
            command=self._handle_generate_password
        )

        create_password_button = ttk.Button(
            master=self._frame,
            text="Add",
            command=self._handle_create_password
        )

        self._create_password_input_app.grid(row=3,column=0,padx=(100,5),pady=(5,2),sticky=constants.EW)
        self._create_password_input_password.grid(row=3,column=1,padx=(5,5),pady=(5,2),sticky=constants.EW)
        autogenerate_password_button.grid(row=3,column=2,padx=(5,5),pady=(5,2),sticky=constants.EW)
        create_password_button.grid(row=3,column=3,padx=(5,100),pady=(5,2),sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master = self._frame,
            textvariable=self._error_variable,
            font=self._error_font,
            foreground="red"
        )

        self._error_placeholder_label = ttk.Label(
            master=self._frame, 
            text="", 
            font=self._error_font,
            foreground="red"
        )

        self._password_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_password_list()
        self._initialize_footer()

        self._password_list_frame.grid(
            row=2,
            column=0,
            columnspan=4,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0,weight=0,minsize=100)
        self._frame.grid_columnconfigure(1,weight=1,minsize=200)
        self._frame.grid_columnconfigure(2,weight=0)

        self._error_placeholder_label.grid(row=4, column=1, padx=(5,5),pady=(2,40), sticky=constants.W)
        self._error_label.grid(row=4, column=0, padx=(100,2), pady=(2,40), sticky=constants.W)

        self._hide_error()