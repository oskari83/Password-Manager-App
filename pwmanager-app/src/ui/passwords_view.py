from tkinter import ttk, constants
from services.user_service import user_service

class PasswordListView:
    def __init__(self, root, passwords, handle_delete_password):
        self._root = root
        self._passwords = passwords
        self._handle_delete_password = handle_delete_password
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_password_item(self, password):
        item_frame = ttk.Frame(master=self._frame)
        labelApp = ttk.Label(master=item_frame,text=password.app)
        labelPassword = ttk.Label(master=item_frame,text=password.password)

        delete_password_button = ttk.Button(master=item_frame,text="Delete",command=lambda: self._handle_delete_password(password.app))
        
        labelApp.grid(row=0,column=0,padx=(100,5),pady=5,sticky=constants.W)
        labelPassword.grid(row=0,column=1,padx=(5,5),pady=5,sticky=constants.W)
        delete_password_button.grid(row=0,column=2,padx=(5,100),pady=5,sticky=constants.EW)

        item_frame.grid_columnconfigure(0,weight=1,minsize=100)
        item_frame.grid_columnconfigure(1,weight=1,minsize=400)
        item_frame.grid_columnconfigure(2,weight=0)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        
        for pw in self._passwords:
            self._initialize_password_item(pw)

class PasswordsView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._user = user_service.get_current_user()
        self._frame = None
        self._create_password_input_password = None
        self._create_password_input_app = None
        self._password_list_frame = None
        self._password_list_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        user_service.logout()
        self._handle_logout()

    def _handle_delete_password(self, password_app):
        user_service.delete_password(password_app)
        self._initialize_password_list()

    def _initialize_password_list(self):
        if self._password_list_view:
            self._password_list_view.destroy()

        passwords = user_service.get_all_user_passwords()

        self._password_list_view = PasswordListView(
            self._password_list_frame,
            passwords,
            self._handle_delete_password
        )

        self._password_list_view.pack()

    def _initialize_header(self):
        user_label = ttk.Label(master=self._frame, text=f"Logged in: {self._user.username}")
        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command = self._logout_handler
        )

        user_label.grid(row=0,column=0,padx=(100,5),pady=(40,5),sticky=constants.W)
        logout_button.grid(row=0, column=2, padx=(5,100),pady=(40,5),sticky=constants.EW)
    
    def _handle_create_password(self):
        password_item_password = self._create_password_input_password.get()
        password_item_app = self._create_password_input_app.get()
        if password_item_password and password_item_app:
            user_service.add_password(password_item_app,password_item_password)
            self._initialize_password_list()
            self._create_password_input_password.delete(0,constants.END)
            self._create_password_input_app.delete(0,constants.END)

    def _initialize_footer(self):
        self._create_password_input_app = ttk.Entry(master=self._frame)
        self._create_password_input_password = ttk.Entry(master=self._frame)

        create_password_button = ttk.Button(
            master=self._frame,
            text="Add",
            command=self._handle_create_password
        )

        self._create_password_input_app.grid(row=2,column=0,padx=(100,5),pady=(5,40),sticky=constants.EW)
        self._create_password_input_password.grid(row=2,column=1,padx=(5,5),pady=(5,40),sticky=constants.EW)
        create_password_button.grid(row=2,column=2,padx=(5,100),pady=(5,40),sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._password_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_password_list()
        self._initialize_footer()

        self._password_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0,weight=0,minsize=100)
        self._frame.grid_columnconfigure(1,weight=1,minsize=400)
        self._frame.grid_columnconfigure(2,weight=0)