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
        self._current_user = None

    def create_account(self,username_input, password_input):
        username_not_available = self._user_repo.find_user(username_input)
        if username_not_available:
            return "Error, username is taken"
        new_user = User(username_input,password_input)
        self._user_repo.insert_user(new_user)
        return "Account created successfully"

    def authenticate(self, username, password_input):
        user_account = self._user_repo.find_user(username)
        if not user_account or user_account.password!=password_input:
            return None
        self._current_user = user_account
        return user_account

    def add_password(self, app_input,password_input):
        if not self._current_user:
            return None
        new_pass = Password(app_input,password_input,self._current_user.username)
        self._password_repo.insert_password(new_pass)
        return new_pass

    def delete_password(self, app_input):
        if not self._current_user:
            return None
        password_item = self._password_repo.find_password(app_input, self._current_user.username)
        if not password_item:
            return "Could not find such password item"
        self._password_repo.delete_password(password_item)
        return "Password entry deleted successfully"

    def get_all_user_passwords(self):
        pw_list = self._password_repo.find_all(self._current_user.username)
        return pw_list
