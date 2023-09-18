#!/usr/bin/python3
""" Unittest for the console """
from console import HBNBCommand
import unittest
from io import StringIO
from unittest.mock import patch 
from models.engine.db_storage import DBStorage
from models import storage


class TestConsole(unittest.TestCase):
    """ Test for the console """

    def test_create(self):
        """ Test for create """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State name=\"California\"")
            state_id = f.getvalue()
            city_id = f.getvalue()
            self.assertEqual(type(state_id), str)
            self.assertEqual(type(city_id), str)

    def test_show(self):
        """ Test for show """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

        @unittest.skipIf(type(storage) == DBStorage, "not testing db storage")
        def test_show_2(self):
            with patch('sys.stdout', new=StringIO(), ) as f:
                HBNBCommand().onecmd("show State 1234-1234-1234")
                self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_destroy(self):
        """ Test for destroy """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy State")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy State 1234-1234-1234")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_all(self):
        """ Test for all """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all State")
            self.assertEqual(type(f.getvalue()), str)
