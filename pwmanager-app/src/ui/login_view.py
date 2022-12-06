from tkinter import ttk, StringVar, constants
from services.user_service import user_service

class LoginView:
    def __init__(self, root, login_handler, show_create_account_view_handler):
        self._root = root
        self._login_handler = login_handler
        self._show_create_account_view_handler = show_create_account_view_handler

        self._frame = None
        self._username_input = None
        self._password_input = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_login(self):
        username = self._username_input.get()
        password = self._password_input.get()

        response = user_service.authenticate(username,password)
        if response is not None:
            self._login_handler()
        else:
            #implement error
            pass

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_input = ttk.Entry(master=self._frame)
        username_label.grid(padx=100, pady=(2,2),sticky=constants.W)
        self._username_input.grid(padx=100, pady=0,sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_input = ttk.Entry(master=self._frame)
        password_label.grid(padx=100, pady=(5,2),sticky=constants.W)
        self._password_input.grid(padx=100, pady=0,sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        view_label = ttk.Label(master=self._frame, text="Authenticate")
        view_label.grid(padx=100, pady=(40,15),sticky=constants.W)

        self._initialize_username_field()
        self._initialize_password_field()

        login_button = ttk.Button(
            master = self._frame,
            text="Login",
            command=self._handle_login
        )

        create_account_button = ttk.Button(
            master = self._frame,
            text="Create Account",
            command=self._show_create_account_view_handler
        )

        self._frame.grid_columnconfigure(0,weight=1,minsize=400)
        login_button.grid(padx=100, pady=(10,2), sticky=constants.EW)
        create_account_button.grid(padx=100, pady=(0,50), sticky=constants.EW)