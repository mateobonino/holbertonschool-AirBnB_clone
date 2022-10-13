#!/usr/bin/python3


import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_save(self):
        obj = BaseModel()
        test1 = obj.created_at
        test2 = obj.updated_at
        obj.save()
        self.assertEqual(test1, obj.created_at)
        self.assertNotEqual(test2, obj.updated_at)