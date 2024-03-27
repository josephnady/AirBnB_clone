#!/usr/bin/python3
"""
Contains the TestPlaceDocs classes
"""
from models import place
from models.base_model import BaseModel
import unittest
Place = place.Place


class TestPlace(unittest.TestCase):
    """Test the Place class"""
    def test_is_subclass(self):
        """Test that Place is a subclass of BaseModel"""
        test_place = Place()
        self.assertIsInstance(test_place, BaseModel)
        self.assertTrue(hasattr(test_place, "id"))
        self.assertTrue(hasattr(test_place, "created_at"))
        self.assertTrue(hasattr(test_place, "updated_at"))

    def test_city_id_attr(self):
        """Test Place has attr city_id, and it's an empty string"""
        test_place = Place()
        self.assertTrue(hasattr(test_place, "city_id"))
        self.assertEqual(test_place.city_id, "")

    def test_user_id_attr(self):
        """Test Place has attr user_id, and it's an empty string"""
        test_place = Place()
        self.assertTrue(hasattr(test_place, "user_id"))
        self.assertEqual(test_place.user_id, "")

    def test_name_attr(self):
        """Test Place has attr name, and it's an empty string"""
        test_place = Place()
        self.assertTrue(hasattr(test_place, "name"))
        self.assertEqual(test_place.name, "")

    def test_description_attr(self):
        """Test Place has attr description, and it's an empty string"""
        test_place = Place()
        self.assertTrue(hasattr(test_place, "description"))
        self.assertEqual(test_place.description, "")

    def test_number_rooms_attr(self):
        """Test Place has attr number_rooms, and it's an int == 0"""
        test_place = Place()
        self.assertTrue(hasattr(test_place, "number_rooms"))
        self.assertEqual(type(test_place.number_rooms), int)
        self.assertEqual(test_place.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """Test Place has attr number_bathrooms, and it's an int == 0"""
        test_place = Place()
        self.assertTrue(hasattr(test_place, "number_bathrooms"))
        self.assertEqual(type(test_place.number_bathrooms), int)
        self.assertEqual(test_place.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """Test Place has attr max_guest, and it's an int == 0"""
        test_place = Place()
        self.assertTrue(hasattr(test_place, "max_guest"))
        self.assertEqual(type(test_place.max_guest), int)
        self.assertEqual(test_place.max_guest, 0)

    def test_price_by_night_attr(self):
        """Test Place has attr price_by_night, and it's an int == 0"""
        test_place = Place()
        self.assertTrue(hasattr(test_place, "price_by_night"))
        self.assertEqual(type(test_place.price_by_night), int)
        self.assertEqual(test_place.price_by_night, 0)

    def test_latitude_attr(self):
        """Test Place has attr latitude, and it's a float == 0.0"""
        test_place = Place()
        self.assertTrue(hasattr(test_place, "latitude"))
        self.assertEqual(type(test_place.latitude), float)
        self.assertEqual(test_place.latitude, 0.0)

    def test_longitude_attr(self):
        """Test Place has attr longitude, and it's a float == 0.0"""
        test_place = Place()
        self.assertTrue(hasattr(test_place, "longitude"))
        self.assertEqual(type(test_place.longitude), float)
        self.assertEqual(test_place.longitude, 0.0)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        test_place = Place()
        string = "[Place] ({}) {}".format(test_place.id, test_place.__dict__)
        self.assertEqual(string, str(test_place))


if __name__ == "__main__":
    unittest.main()
