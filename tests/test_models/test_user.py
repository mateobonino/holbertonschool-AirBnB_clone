#!/usr/bin/python3

from models.user import User
import unittest


class TestUser(unittest.TestCase):
    def test_user_email(self):
        self.assertEqual(str, type(User.email))

    def test_user_password(self):
        self.assertEqual(str, type(User.password))

    def test_user_first_name(self):
        self.assertEqual(str, type(User.first_name))

    def test_user_last_name(self):
        self.assertEqual(str, type(User.last_name))