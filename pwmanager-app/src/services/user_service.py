from entities.user import User
from entities.password import Password

from repositories.user_repository import (
    user_repository as default_user_repository
)

from repositories.password_repository import (
    password_repository as default_password_repository
)

class UserService:
	def __init__(self):
		self._user_repo = default_user_repository
		self._password_repo = default_password_repository
		self._logged_in = False
		self._currentUser = None

	def create_account(self,usernameInput, passwordInput):
		usernameNotAvailable = self._user_repo.find_user(usernameInput)
		if usernameNotAvailable:
			return "Error, username is taken"
		newUser = User(usernameInput,passwordInput)
		self._user_repo.insert_user(newUser)
		return "Account created successfully"

	def authenticate(self, username, passwordInput):
		userAccount = self._user_repo.find_user(username)
		if not userAccount or userAccount.password!=passwordInput:
			return None
		self._currentUser = userAccount
		return userAccount

	def add_password(self, appInput,passwordInput):
		if not self._currentUser:
			return None
		newPass = Password(appInput,passwordInput,self._currentUser.username)
		self._password_repo.insert_password(newPass)

	def delete_password(self, appInput):
		if not self._currentUser:
			return None
		passwordItem = self._password_repo.find_password(appInput, self._currentUser.username)
		if not passwordItem:
			return "Could not find such password item"
		self._password_repo.delete_password(passwordItem)
		return "Password entry deleted successfully"

	def get_all_user_passwords(self):
		pwList = self._password_repo.find_all(self._currentUser.username)
		return pwList
		