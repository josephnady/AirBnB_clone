#!/usr/bin/python3
"""
Contains the TestStateDocs classes
"""

from models import state
from models.base_model import BaseModel
import unittest
State = state.State


class TestState(unittest.TestCase):
    """Test the State class"""
    def test_is_subclass(self):
        """Test that State is a subclass of BaseModel"""
        test_state = State()
        self.assertIsInstance(test_state, BaseModel)
        self.assertTrue(hasattr(test_state, "id"))
        self.assertTrue(hasattr(test_state, "created_at"))
        self.assertTrue(hasattr(test_state, "updated_at"))

    def test_name_attr(self):
        """Test that State has attribute name, and it's as an empty string"""
        test_state = State()
        self.assertTrue(hasattr(test_state, "name"))
        self.assertEqual(test_state.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        s = State()
        new_d = s.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = State()
        new_d = s.to_dict()
        self.assertEqual(new_d["__class__"], "State")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], s.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], s.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        test_state = State()
        string = "[State] ({}) {}".format(test_state.id, test_state.__dict__)
        self.assertEqual(string, str(test_state))


if __name__ == "__main__":
    unittest.main()
