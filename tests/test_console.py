#!/usr/bin/python3
""" Unittest for the console """
from console import HBNBCommand
import unittest
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """ Test for the console """

    def test_create(self):
        """ Test for create """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)

    def test_show(self):
        """ Test for show """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)

    def test_destroy(self):
        """ Test for destroy """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)

    def test_all(self):
        """ Test for all """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)

    def test_update(self):
        """ Test for update """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertTrue(len(f.getvalue()) > 0)

    def test_quit(self):
        """ Test for quit """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """ Test for EOF """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_help(self):
        """ Test for help """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertTrue(len(f.getvalue()) > 0)

    def test_emptyline(self):
        """ Test for emptyline """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))