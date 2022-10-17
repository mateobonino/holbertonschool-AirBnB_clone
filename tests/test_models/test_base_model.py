#!/usr/bin/python3
"""Test cases for BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_save(self):
        """Tests the save method"""
        obj = BaseModel()
        test1 = obj.created_at
        test2 = obj.updated_at
        obj.save()
        self.assertEqual(test1, obj.created_at)
        self.assertNotEqual(test2, obj.updated_at)

    def test_str(self):
        """Tests the __str__ method"""
        self.assertEqual(str, type(str(BaseModel)))

    def test_to_dict(self):
        """Tests the to_dict method"""
        obj = BaseModel()
        obj_dict = {'id': obj.id, 'created_at': obj.created_at, 'updated_at': obj.updated_at, '__class__': obj.__class__.__name__}
        self.assertEqual(dict, type(obj.to_dict()))
