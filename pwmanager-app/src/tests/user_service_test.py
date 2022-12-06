import unittest
from services.user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.service = UserService()
        self.service._user_repo.delete_all()
        self.service._password_repo.delete_all()

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

    def test_password_addition_works(self):
        self.service.create_account("username5","password5")
        self.service.authenticate("username5","password5")
        response = self.service.add_password("testApp", "superSafePassword")
        self.assertEqual(response.app,"testApp")

    def test_password_removal_works(self):
        self.service.create_account("username5","password5")
        self.service.authenticate("username5","password5")
        self.service.add_password("testApp", "superSafePassword")
        response = self.service.delete_password("testApp")
        self.assertEqual(response,"Password entry deleted successfully")