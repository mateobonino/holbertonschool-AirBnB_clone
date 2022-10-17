#!/usr/bin/python3
"""test city"""
import unittest
from models.city import City


class BaseModelClass(unittest.TestCase):
    """Test city"""
    def test_city(self):
        instance = City()
        self.assertEqual(instance.name, '')
        self.assertEqual(instance.state_id, '')
