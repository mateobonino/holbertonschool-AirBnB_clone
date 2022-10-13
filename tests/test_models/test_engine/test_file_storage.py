#!/usr/bin/python3

from models.engine.file_storage import FileStorage
import unittest

class TestFileStorage(unittest.TestCase):
    def test_all(self):
        obj = FileStorage()
        self.assertTrue(hasattr(obj, 'all'), True)
        self.assertTrue(hasattr(obj, 'save'), True)
        self.assertTrue(hasattr(obj, 'new'), True)
        self.assertTrue(hasattr(obj, 'reload'), True)