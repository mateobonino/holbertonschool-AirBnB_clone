#!/usr/bin/python3
"""test place"""
import unittest
from models.amenity import Place


class BaseModelClass(unittest.TestCase):
    """Test place"""
    def test_city(self):
        instance = Place()
        self.assertEqual(instance.city_id, '')
        self.assertEqual(instance.user_id, '')
        self.assertEqual(instance.name, '')
        self.assertEqual(instance.description, '')
        self.assertEqual(instance.number_rooms, 0)
        self.assertEqual(instance.number_bathrooms, 0)
        self.assertEqual(instance.max_guest, 0)
        self.assertEqual(instance.price_by_night, 0)
        self.assertEqual(instance.latitude, 0.0)
        self.assertEqual(instance.longitude, 0.0)
        self.assertEqual(instance.amenity_ids, [])
