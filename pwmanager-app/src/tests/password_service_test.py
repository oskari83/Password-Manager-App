import unittest
from entities.user import User
from entities.password import Password
from services.password_service import PasswordService

class TestPasswordService(unittest.TestCase):
    def setUp(self):
        self.service = PasswordService(1)
        self.service._password_repo.delete_all()

    def test_password_addition_works(self):
        self.service.set_user(User("username5","password5"))
        response = self.service.add_password("testApp", "superSafePassword")
        self.assertEqual(response.app,"testApp")

    def test_password_addition_doesnt_work_if_not_logged_in(self):
        response = self.service.add_password("testApp", "superSafePassword")
        self.assertEqual(response,None)

    def test_password_addition_doesnt_work_if_already_exists(self):
        self.service.set_user(User("username5","password5"))
        self.service.add_password("testApp", "superSafePassword")
        response = self.service.add_password("testApp", "anotherOne")
        self.assertEqual(response,"App with that name already exists in the database")

    def test_password_removal_works(self):
        self.service.set_user(User("username5","password5"))
        self.service.add_password("testApp", "superSafePassword")
        response = self.service.delete_password("testApp")
        self.assertEqual(response,"Password entry deleted successfully")

    def test_password_deletion_doesnt_work_if_not_logged_in(self):
        self.service.set_user(User("username5","password5"))
        self.service.add_password("testApp", "superSafePassword")
        self.service.remove_user()
        response = self.service.delete_password("testApp")
        self.assertEqual(response,None)

    def test_password_updating_works(self):
        self.service.set_user(User("username5","password5"))
        response = self.service.add_password("testApp", "superSafePassword")
        self.assertEqual(response.password,"superSafePassword")
        self.service.change_password(Password("testApp", "newPassword", "username5"))
        pwlist = self.service.get_all_user_passwords()
        self.assertEqual(pwlist[0].password,"newPassword")

    def test_password_updating_doesnt_work_if_not_logged_in(self):
        self.service.set_user(User("username5","password5"))
        response = self.service.add_password("testApp", "superSafePassword")
        self.assertEqual(response.password,"superSafePassword")
        self.service.remove_user()
        response = self.service.change_password(Password("testApp", "newPassword", "username5"))
        self.assertEqual(response,None)

    def test_password_list_return_works(self):
        self.service.set_user(User("username5","password5"))
        self.service.add_password("testApp", "superSafePassword")
        self.service.add_password("testApp2", "superSafePassword2")
        pwlist = self.service.get_all_user_passwords()
        self.assertEqual(len(pwlist),2)