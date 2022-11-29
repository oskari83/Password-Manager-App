import unittest
from services.user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.service = UserService()
        self.service._user_repo.delete_all()
        self.service._password_repo.delete_all()

    def test_account_creation(self):
        response = self.service.create_account("username2","password2")
        self.assertEqual(response, "Account created successfully")

    def test_cannot_create_duplicate_account(self):
        self.service.create_account("username3","password3")
        response = self.service.create_account("username3","password333")
        self.assertEqual(response, "Error, username is taken")
    
    def test_login(self):
        self.service.create_account("username2","password2")
        response = self.service.authenticate("username2","password2")
        self.assertEqual(response.username, "username2")

    def test_login_fails_with_incorrect_password(self):
        self.service.create_account("username2","password2")
        response = self.service.authenticate("username2","vaarasalasana")
        self.assertEqual(response, None)