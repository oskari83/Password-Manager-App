from tkinter import ttk, constants, StringVar
from tkinter.font import BOLD, Font
from services.user_service import user_service
import random, string

class PasswordListView:
    def __init__(self, master_root, root, passwords, handle_delete_password):
        self._master_root = master_root
        self._root = root
        self._passwords = passwords
        self._handle_delete_password = handle_delete_password
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _copy_to_clipboard_handler(self, text):
        self._master_root.clipboard_clear()
        self._master_root.clipboard_append(text)
        self._master_root.update()

    def _initialize_password_item(self, password):
        item_frame = ttk.Frame(master=self._frame)
        labelApp = ttk.Label(master=item_frame,text=f"{password.app}:")
        labelPassword = ttk.Label(master=item_frame,text=password.password)

        copy_to_clipboard_button = ttk.Button(master=item_frame,text="Copy",command=lambda: self._copy_to_clipboard_handler(password.password))
        delete_password_button = ttk.Button(master=item_frame,text="Delete",command=lambda: self._handle_delete_password(password.app))
        
        labelApp.grid(row=0,column=0,padx=(100,5),pady=5,sticky=constants.EW)
        labelPassword.grid(row=0,column=1,padx=(5,5),pady=5,sticky=constants.EW)
        copy_to_clipboard_button.grid(row=0,column=2,padx=(5,5),pady=5,sticky=constants.EW)
        delete_password_button.grid(row=0,column=3,padx=(5,100),pady=5,sticky=constants.EW)

        item_frame.grid_columnconfigure(0,weight=0,minsize=100)
        item_frame.grid_columnconfigure(1,weight=1,minsize=200)
        item_frame.grid_columnconfigure(2,weight=0)
        item_frame.grid_columnconfigure(3,weight=0)
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

        self._error_variable = None
        self._error_label = None

        self._error_font = Font(self._root, size=8)
        self._bold10 = Font(self._root, size=10, weight=BOLD)

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()
    
    def _hide_error(self):
        self._error_label.grid_remove()

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
            self._root,
            self._password_list_frame,
            passwords,
            self._handle_delete_password
        )

        self._password_list_view.pack()

    def _initialize_header(self):
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
        password_item_password = self._create_password_input_password.get()
        password_item_app = self._create_password_input_app.get()

        if len(password_item_password) == 0 or len(password_item_app) == 0:
            self._show_error("Empty app name or password")
            return

        if password_item_password and password_item_app:
            user_service.add_password(password_item_app,password_item_password)
            self._hide_error()
            self._initialize_password_list()
            self._create_password_input_password.delete(0,constants.END)
            self._create_password_input_app.delete(0,constants.END)

    def _handle_generate_password(self):
        generated_password = "".join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) for _ in range(16))
        self._create_password_input_password.delete(0, constants.END)
        self._create_password_input_password.insert(0, generated_password)

    def _initialize_footer(self):
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