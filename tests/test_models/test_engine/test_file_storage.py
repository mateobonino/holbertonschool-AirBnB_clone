#!/usr/bin/python3

from models.engine.file_storage import FileStorage
import unittest

class TestFileStorage(unittest.TestCase):
    def test_all(self):
        obj = FileStorage()
        self.assertEqual(hasattr(obj, 'all'), True)