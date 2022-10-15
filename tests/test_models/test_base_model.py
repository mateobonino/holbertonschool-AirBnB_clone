#!/usr/bin/python3


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_save(self):
        obj = BaseModel()
        test1 = obj.created_at
        test2 = obj.updated_at
        obj.save()
        self.assertEqual(test1, obj.created_at)
        self.assertNotEqual(test2, obj.updated_at)

    def test_str(self):
        self.assertEqual(str, type(str(BaseModel)))

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = {'id': obj.id, 'created_at': obj.created_at, 'updated_at': obj.updated_at, '__class__': obj.__class__.__name__}
        # self.assertEqual(obj.to_dict(), '')
