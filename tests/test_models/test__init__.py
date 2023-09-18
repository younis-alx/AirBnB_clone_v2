from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.__init__ import storage
import unittest
import pep8


class TestFileStorage(unittest.TestCase):
    """ tests for file storage """

    def test_pep8_conformance_file_storage(self):
        """Test that models/engine/file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """Test that tests/test_models/test_engine/test_file_storage.py
        conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring(self):
        """test docstring"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_storage_type(self):
        """test storage type"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.assertEqual(type(storage), DBStorage)
        elif getenv("HBNB_TYPE_STORAGE") == "file":
            self.assertEqual(type(storage), FileStorage)
