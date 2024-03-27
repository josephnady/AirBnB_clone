#!/usr/bin/python3
"""
Contains the TestReviewDocs classes
"""
from models import review
from models.base_model import BaseModel
import unittest
Review = review.Review


class TestReview(unittest.TestCase):
    """Test the Review class"""
    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        test_review = Review()
        self.assertIsInstance(test_review, BaseModel)
        self.assertTrue(hasattr(test_review, "id"))
        self.assertTrue(hasattr(test_review, "created_at"))
        self.assertTrue(hasattr(test_review, "updated_at"))

    def test_place_id_attr(self):
        """Test Review has attr place_id, and it's an empty string"""
        test_review = Review()
        self.assertTrue(hasattr(test_review, "place_id"))
        self.assertEqual(test_review.place_id, "")

    def test_user_id_attr(self):
        """Test Review has attr user_id, and it's an empty string"""
        test_review = Review()
        self.assertTrue(hasattr(test_review, "user_id"))
        self.assertEqual(test_review.user_id, "")

    def test_text_attr(self):
        """Test Review has attr text, and it's an empty string"""
        test_review = Review()
        self.assertTrue(hasattr(test_review, "text"))
        self.assertEqual(test_review.text, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(new_d["__class__"], "Review")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        test_review = Review()
        string = "[Review] ({}) {}".format(
                test_review.id, test_review.__dict__)
        self.assertEqual(string, str(test_review))


if __name__ == "__main__":
    unittest.main()
