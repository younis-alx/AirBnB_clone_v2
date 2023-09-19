#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import os
import unittest
from unittest.mock import patch
from models.base_model import BaseModel


@unittest.skipIf(os.getenv(
    'HBNB_TYPE_STORAGE') == 'db', "Testing DBStorage only")
class test_review(test_basemodel):
    """ test the review class"""

    def __init__(self, *args, **kwargs):
        """ initializes class
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Attributes:
            name: name of the class
            value: object of the class

        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ test if place_id is a string"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ test if user_id is a string"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ test if text is a string"""
        new = self.value()
        self.assertEqual(type(new.text), str)


class test_review2(unittest.TestCase):
    """this will test the review class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.review = Review()
        cls.review.place_id = "1234-abcd"
        cls.review.user_id = "4321-dcba"
        cls.review.text = "This place is nice"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.review

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring(self):
        """checking for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes(self):
        """chekcing if review have attributes"""
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)

    def test_subclass(self):
        """test if review inherits from BaseModel"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_attribute_types(self):
        """test attribute type for review"""
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """test if save works"""
        self.review.save()
        self.assertTrue(mock_storage.save.called)

    def test_to_dict(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.review), True)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """test if save works"""
        self.review.save()
        self.assertTrue(mock_storage.save.called)
