#!/usr/bin/python3
"""test state"""
import unittest
from models.state import State


class BaseModelClass(unittest.TestCase):
    """Test state"""
    def test_state(self):
        instance = state()
        elf.assertEqual(instance.name, '')
