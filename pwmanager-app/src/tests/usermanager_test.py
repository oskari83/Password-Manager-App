import unittest
from usermanager import UserManager, UserDatabase

class TestUsermanager(unittest.TestCase):
    def setUp(self):
        self.db = UserDatabase()
        self.service = UserManager(self.db)

    def test_account_creation(self):
        self.service.create_account("username2","password2")
        self.assertEqual(self.service.grab_user("username2").get_username(), "username2")
    
    def test_login(self):
        self.service.create_account("username2","password2")
        response = self.service.authenticate(self.service.grab_user("username2"),"password2")
        self.assertEqual(response, "Authentication successful!")