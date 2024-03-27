#!/usr/bin/python3
"""
Contains the TestCityDocs classes
"""
from models import city
from models.base_model import BaseModel
import unittest
City = city.City


class TestCity(unittest.TestCase):
    """Test the City class"""
    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        cit = City()
        self.assertIsInstance(cit, BaseModel)
        self.assertTrue(hasattr(cit, "id"))
        self.assertTrue(hasattr(cit, "created_at"))
        self.assertTrue(hasattr(cit, "updated_at"))

    def test_name_attr(self):
        """Test that City has attribute name, and it's an empty string"""
        cit = City()
        self.assertTrue(hasattr(cit, "name"))
        self.assertEqual(cit.name, "")

    def test_state_id_attr(self):
        """Test that City has attribute state_id, and it's an empty string"""
        cit = City()
        self.assertTrue(hasattr(cit, "state_id"))
        self.assertEqual(cit.state_id, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        c = City()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = City()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "City")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        cit = City()
        string = "[City] ({}) {}".format(cit.id, cit.__dict__)
        self.assertEqual(string, str(cit))


if __name__ == "__main__":
    unittest.main()
