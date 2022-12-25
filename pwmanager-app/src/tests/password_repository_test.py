import unittest
from repositories.password_repository import PasswordRepository
from database_connection import get_test_database_connection
from entities.password import Password

def get_user_by_row(row):
    return Password(row["app"], row["password"], row["username"]) if row else None

class TestPasswordRepository(unittest.TestCase):
    def setUp(self):
        self.repo = PasswordRepository(get_test_database_connection())
        self.repo.delete_all()

    def test_find_all_returns_correct_amount(self):
        self.repo.insert_password(Password("google", "salasana1", "user1"))
        self.repo.insert_password(Password("youtube", "salasana2", "user1"))
        self.repo.insert_password(Password("twitter", "salasana3", "user1"))
        self.assertEqual(len(self.repo.find_all("user1")), 3)

    def test_finds_specific_password(self):
        self.repo.insert_password(Password("google", "salasana1", "user1"))
        response = self.repo.find_password("google", "user1")
        self.assertEqual(response.password, "salasana1")

    def test_doesnt_find_nonexistent_password(self):
        self.repo.insert_password(Password("google", "salasana1", "user1"))
        response = self.repo.find_password("twitch", "user1")
        self.assertEqual(response, None)

    def test_deleting_all_works_correctly(self):
        self.repo.insert_password(Password("google", "salasana1", "user1"))
        self.repo.insert_password(Password("youtube", "salasana2", "user1"))
        self.repo.insert_password(Password("twitter", "salasana3", "user1"))
        self.repo.delete_all()
        self.assertEqual(len(self.repo.find_all("user1")), 0)

    def test_updating_password_works(self):
        self.repo.insert_password(Password("google", "salasana1", "user1"))
        response = self.repo.find_password("google", "user1")
        self.assertEqual(response.password, "salasana1")
        self.repo.update_password(Password("google", "uusisalasana", "user1"))
        response = self.repo.find_password("google", "user1")
        self.assertEqual(response.password, "uusisalasana")