#!/usr/bin/python3
"""test amenity"""
import unittest
from models.amenity import Amenity


class BaseModelClass(unittest.TestCase):
    """Test amenity"""
    def test_amenity(self):
        instance = Amenity()
        self.assertEqual(instance.name, '')
