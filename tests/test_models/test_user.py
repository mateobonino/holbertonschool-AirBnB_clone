#!/usr/bin/python3
"""Test cases for User Class"""


from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Test cases for User Class"""
    def test_user_email(self):
        """Checks if the email attribute is a string"""
        self.assertEqual(str, type(User.email))

    def test_user_password(self):
        """Checks if the password attribute is a string"""
        self.assertEqual(str, type(User.password))

    def test_user_first_name(self):
        """Checks if the user first name attribute is a string"""
        self.assertEqual(str, type(User.first_name))

    def test_user_last_name(self):
        """Checks if the user last name attribute is a string"""
        self.assertEqual(str, type(User.last_name))
