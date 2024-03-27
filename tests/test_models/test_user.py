#!/usr/bin/python3
"""
Contains the TestUserDocs classes
"""
from models import user
from models.base_model import BaseModel
import unittest
User = user.User


class TestUser(unittest.TestCase):
    """Test the User class"""
    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel"""
        test_user = User()
        self.assertIsInstance(test_user, BaseModel)
        self.assertTrue(hasattr(test_user, "id"))
        self.assertTrue(hasattr(test_user, "created_at"))
        self.assertTrue(hasattr(test_user, "updated_at"))

    def test_email_attr(self):
        """Test that User has attr email, and it's an empty string"""
        test_user = User()
        self.assertTrue(hasattr(test_user, "email"))
        self.assertEqual(test_user.email, "")

    def test_password_attr(self):
        """Test that User has attr password, and it's an empty string"""
        test_user = User()
        self.assertTrue(hasattr(test_user, "password"))
        self.assertEqual(test_user.password, "")

    def test_first_name_attr(self):
        """Test that User has attr first_name, and it's an empty string"""
        test_user = User()
        self.assertTrue(hasattr(test_user, "first_name"))
        self.assertEqual(test_user.first_name, "")

    def test_last_name_attr(self):
        """Test that User has attr last_name, and it's an empty string"""
        test_user = User()
        self.assertTrue(hasattr(test_user, "last_name"))
        self.assertEqual(test_user.last_name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = User()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "User")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        test_user = User()
        string = "[User] ({}) {}".format(test_user.id, test_user.__dict__)
        self.assertEqual(string, str(test_user))


if __name__ == "__main__":
    unittest.main()
