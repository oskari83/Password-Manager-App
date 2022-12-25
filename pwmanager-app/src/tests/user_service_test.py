import unittest
from services.user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.service = UserService(1)
        self.service._user_repo.delete_all()

    def test_account_creation(self):
        response = self.service.create_account("username2","password2")
        self.assertNotEqual(response, None)
        self.assertEqual(response.username, "username2")

    def test_cannot_create_duplicate_account(self):
        self.service.create_account("username3","password3")
        response = self.service.create_account("username3","password333")
        self.assertEqual(response, None)
    
    def test_login(self):
        self.service.create_account("username2","password2")
        response = self.service.authenticate("username2","password2")
        self.assertEqual(response.username, "username2")

    def test_login_fails_with_incorrect_password(self):
        self.service.create_account("username2","password2")
        response = self.service.authenticate("username2","vaarasalasana")
        self.assertEqual(response, None)

    def test_returns_logged_in_user(self):
        self.service.create_account("username5","password5")
        self.service.authenticate("username5","password5")
        user = self.service.get_current_user()
        self.assertEqual(user.username,"username5")

    def test_logout_works(self):
        self.service.create_account("username5","password5")
        self.service.authenticate("username5","password5")
        user = self.service.get_current_user()
        self.assertEqual(user.username,"username5")
        self.service.logout()
        response = self.service.get_current_user()
        self.assertEqual(response, None)