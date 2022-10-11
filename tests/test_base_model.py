#!/usr/bin/python3

from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    def test_1(self):
        base1 = BaseModel()
        time1 = base1.updated_at
        base1.save()
        time2 = base1.updated_at
        self.assertNotEqual(time1, time2)


