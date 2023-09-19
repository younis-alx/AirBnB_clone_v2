#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import os
import unittest


@unittest.skipIf(os.getenv(
    'HBNB_TYPE_STORAGE') == 'db', "Testing DBStorage only")
class test_User(test_basemodel):
    """ test the user class"""

    def __init__(self, *args, **kwargs):
        """ you know what it is
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Attributes:
            name: name of the class
            value: object of the class
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ test if first_name is a string"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ test if last_name is a string"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ test if email is a string"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ test if password is a string"""
        new = self.value()
        self.assertEqual(type(new.password), str)
