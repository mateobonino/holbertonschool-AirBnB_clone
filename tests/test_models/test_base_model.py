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
        obj = BaseModel()
        obj_name = obj.__class__.__name__
        obj_id = obj.id
        obj_dict = obj.__dict__
        obj_str = f"[{obj_name}] ({obj_id}) {obj_dict}"
        self.assertEqual(str(obj), obj_str)

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = {'id': obj.id, 'created_at': obj.created_at, 'updated_at': obj.updated_at, '__class__': obj.__class__.__name__}
        # self.assertEqual(obj.to_dict(), '')