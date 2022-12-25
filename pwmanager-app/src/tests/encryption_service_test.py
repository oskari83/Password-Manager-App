import unittest
from entities.user import User
from entities.password import Password
from services.encryption_service import EncryptionService

class TestEncryptionService(unittest.TestCase):
    def setUp(self):
        self.service = EncryptionService()

    def test_encryption_return_something_different(self):
        response = self.service.encrypt_password("password")
        self.assertNotEqual(response,"password")

    def test_password_matching_works(self):
        encrypted_password = self.service.encrypt_password("password")
        input_password = "password"
        response = self.service.password_match_comparison(input_password,encrypted_password)
        self.assertEqual(response,True)
