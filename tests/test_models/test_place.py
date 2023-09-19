#!/usr/bin/python3
""" Unittest for Place class """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import os
import unittest


@unittest.skipIf(os.getenv(
    'HBNB_TYPE_STORAGE') == 'db', "Testing DBStorage only")
class test_Place(test_basemodel):
    """ Test the Place class """

    def __init__(self, *args, **kwargs):
        """ Initializes class
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Attributes:
            name: name of the class
            value: object of the class
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ test if city_id is a string """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ test if user_id is a string"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ test if name is a string """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ test if description is a string"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ test if number_rooms is an integer"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ test if number_bathrooms is an integer"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ test if max_guest is an integer"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ test if price_by_night is an integer"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ test if latitude is a float"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ test if longitude is a float"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ test if amenity_ids is a list"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
