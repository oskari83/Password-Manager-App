class User:
	def __init__(self, username, password):
		self._username = username
		self._password = password

	def get_username(self):
		return self._username

	def password_match(self, pwInput):
		return self._password==pwInput

class UserDatabase:
	def __init__(self):
		self._users = []

	def get_users(self):
		return self._users
	
	def add_user(self,user:User):
		self._users.append(user)

	def find_user(self, usernameInput):
		for u in self._users:
			if u.get_username()==usernameInput:
				return u
		return None

class UserManager:
	def __init__(self,db):
		self._database = db
		self._logged_in = False
		self._currentUser = None

	def create_account(self,usernameInput, passwordInput):
		newUser = User(usernameInput,passwordInput)
		self._database.add_user(newUser)
	
	def grab_user(self, usernameInput):
		user = self._database.find_user(usernameInput)
		return user

	def authenticate(self, user, passwordInput):
		if(user and user.password_match(passwordInput)):
			self._logged_in=True
			return "Authentication successful!"
		self._logged_in=False
		return "Error, wrong credentials"