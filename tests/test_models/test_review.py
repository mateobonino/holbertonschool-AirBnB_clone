#!/usr/bin/python3
"""test review"""
import unittest
from models.review import Review


class BaseModelClass(unittest.TestCase):
    """Test review"""
    def test_review(self):
        instance = Review()
        self.assertEqual(instance.place_id, '')
        self.assertEqual(instance.user_id, '')
        self.assertEqual(instance.text, '')
