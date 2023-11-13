#!/usr/bin/python3
"""Test case for Base.py"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle as Rectangle


class TestBaseInit(unittest.TestCase):
    """
    Class to Test for Base init method
    """
    def test_no_argument(self):
        a = Base()
        self.assertEqual(a.id, 1)

    def test_integer(self):
        a = Base(5)
        self.assertEqual(a.id, 5)

    def test_string(self):
        a = Base("string")
        self.assertEqual(a.id, "string")

    def test_float(self):
        a = Base(float("inf"))
        self.assertEqual(a.id, float("inf"))

    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2, 3)


class ToJsonString(unittest.TestCase):
    """Class to test to_json_string method"""
    def test_list(self):
        a = [{'I': 1, 'II': 2}]
        self.assertEqual(Base.to_json_string(a), '[{"I": 1, "II": 2}]')

    def test_empty_list(self):
        a = []
        self.assertEqual(Base.to_json_string(a), '[]')

    def test_none(self):
        a = None
        self.assertEqual(Base.to_json_string(a), '[]')


class SaveToFile(unittest.TestCase):
    """Class to test save_to_file method"""

    @staticmethod
    def del_files():
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_rectangle_list(self):
        a = Rectangle(4, 5, 1, 1, 1)
        b = Rectangle(1, 2, 4, 5, 7)

        Rectangle.save_to_file([a, b])
        with open("Rectangle.json", "r") as file:
            text = file.read()
            file.close()
        self.assertTrue(len(text) == 104)


if __name__ == "__main__":
    # if it is run directly
    unittest.main()
