#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models import storage
import models
import unittest

class TestFileStorage(unittest.TestCase):

    def test__file_path(self):
        obj = FileStorage()
        self.assertEqual(obj._FileStorage__file_path, "file.json")

    def test_objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_reload(self):
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_all(self):
        self.assertEqual(dict, type(storage.all()))
