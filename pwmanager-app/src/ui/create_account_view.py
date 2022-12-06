from tkinter import ttk, constants
from services.user_service import user_service

class CreateAccountView:
    def __init__(self, root, handle_create_account, handle_show_login_view):
        self._root = root
        self._handle_create_account = handle_create_account
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username_input = None
        self._password_input = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _create_account_handler(self):
        username = self._username_input.get()
        password = self._password_input.get()

        if len(username) == 0 or len(password) == 0:
            #implement error
            return
        
        response = user_service.create_account(username,password)
        if response is not None:
            self._handle_create_account()
        else:
            pass
    
    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_input = ttk.Entry(master=self._frame)
        username_label.grid(padx=100, pady=(40,2),sticky=constants.W)
        self._username_input.grid(padx=100, pady=0,sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_input = ttk.Entry(master=self._frame)
        password_label.grid(padx=100, pady=(5,2),sticky=constants.W)
        self._password_input.grid(padx=100, pady=0,sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_username_field()
        self._initialize_password_field()

        create_account_button = ttk.Button(
            master = self._frame,
            text="Create Account",
            command=self._create_account_handler
        )

        login_button = ttk.Button(
            master = self._frame,
            text="Login",
            command=self._handle_show_login_view
        )

        self._frame.grid_columnconfigure(0,weight=1,minsize=400)
        create_account_button.grid(padx=100, pady=(10,2), sticky=constants.EW)
        login_button.grid(padx=100, pady=(0,50), sticky=constants.EW)