from consoleIO import ConsoleIO
from usermanager import UserDatabase,UserManager

class PasswordManagerApp:
	def __init__(self):
		self._io = ConsoleIO()
		self._user_db = UserDatabase()
		self._user_service = UserManager(self._user_db)

	def run(self):
		self.print_initial()

		while True:
			self.print_instructions()
			command = self._io.cin("Command: ")

			if(command=="1"):
				self.login()
			elif(command=="2"):
				self.create_account()
			elif(command=="3"):
				self._io.newline()
				self._io.cout("Bye, see you soon!")
				break


	def print_instructions(self):
		self._io.newline()
		self._io.cout("Welcome, Press:")
		self._io.newline()
		self._io.cout("[1]	To Log-In")
		self._io.cout("[2]	To Create an Account")
		self._io.cout("[3]	To Exit")
		self._io.newline()

	def print_initial(self):
		self._io.cout("-------------------------------------------------")
		self._io.cout("|	Password Manager v1			|")
		self._io.cout("-------------------------------------------------")


	def create_account(self):
		self._io.newline()
		self._io.cout("Please input a username and password to create your account:")
		usernameInput = self._io.cin("Username: ")
		passwordInput = self._io.cin("Password: ")
		check = self._io.cin("Confirm (y/n): ")
		if(check=="" or check=="y" or check=="yes"):
			self._user_service.create_account(usernameInput,passwordInput)
			self._io.newline()
			self._io.cout("Account created successfully, you can now log-in with your credentials!")
		else:
			self._io.cout("No worries, we will cancel that!")

	def login(self):
		self._io.newline()
		self._io.cout("Please input your username and password:")
		usernameInput = self._io.cin("Username: ")
		passwordInput = self._io.cin("Password: ")
		user = self._user_service.grab_user(usernameInput)
		if(user):
			response = self._user_service.authenticate(user,passwordInput)
			self._io.newline()
			self._io.cout(response)
		else:
			self._io.newline()
			self._io.cout("Could not find user matching that username")