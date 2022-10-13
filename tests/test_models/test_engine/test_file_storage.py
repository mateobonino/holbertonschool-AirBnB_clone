#!/usr/bin/python3

from models.engine.file_storage import FileStorage
import unittest

class TestFileStorage(unittest.TestCase):
    def test_all(self):
        obj = FileStorage()
        obj_all = obj._FileStorage__objects
        self.assertEqual(obj.all(), obj_all)

    def test_save(self):
        obj = FileStorage()
        self.assertTrue(hasattr(obj, 'save'), True)

    def test_new(self):
        obj = FileStorage()
        self.assertTrue(hasattr(obj, 'new'), True)

    def test__file_path(self):
        obj = FileStorage()
        self.assertEqual(obj._FileStorage__file_path, "file.json")
