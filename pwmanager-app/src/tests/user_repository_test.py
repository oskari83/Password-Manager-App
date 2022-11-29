import unittest
from repositories.user_repository import UserRepository
from database_connection import get_database_connection
from entities.user import User

def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.repo = UserRepository(get_database_connection())
        self.repo.delete_all()

    def test_find_all_returns_correct_amount(self):
        self.repo.insert_user(User("username1","password"))
        self.repo.insert_user(User("username2","password"))
        self.repo.insert_user(User("username3","password"))
        self.assertEqual(len(self.repo.find_all()), 3)
