#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel, BaseModel
from models.state import State
from unittest.mock import patch
from io import StringIO
import unittest
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Testing DBStorage only")
class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class test_state2(unittest.TestCase):
    """this will test the state class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.state = State()
        cls.state.name = "California"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.state

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_docstring(self):
        """checking for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes(self):
        """chekcing if State have attributes"""
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass(self):
        """test if State is subclass of Basemodel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types(self):
        """test attribute type for State"""
        self.assertEqual(type(self.state.name), str)

    def test_save(self):
        """test if the save works"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.state), True)

    @patch('sys.stdout', new_callable=StringIO)
    def test_str(self, mock_stdout):
        """test str"""
        expected = "[{}] ({}) {}\n".format(self.state.__class__.__name__,
                                           self.state.id, self.state.__dict__)
        print(self.state)
        self.assertEqual(mock_stdout.getvalue(), expected)
