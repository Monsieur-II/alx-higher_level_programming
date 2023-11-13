#!/usr/bin/python3
"""Test case for Base.py"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle as Rectangle
from models.square import Square


class TestBaseInit(unittest.TestCase):
    """
    Class to Test for Base init method
    """
    def test_no_argument(self):
        a = Base()
        b = Base()
        self.assertEqual(b.id, a.id + 1)

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
            self.assertTrue(len(file.read()) == 104)
            file.close()

    def test_square_list(self):
        a = Square(4, 1, 3, 'e1')
        b = Square(6, 0, 2, 'e2')
        Square.save_to_file([a, b])

        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 82)


class TestFromJsonString(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)


class TestBaseCreate(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))


class TestLoadFromFile(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

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

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    class TestBaseLoadFromFile(unittest.TestCase):
        """Unittests for testing load_from_file_method of Base class."""

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

        def test_load_from_file_first_rectangle(self):
            r1 = Rectangle(10, 7, 2, 8, 1)
            r2 = Rectangle(2, 4, 5, 6, 2)
            Rectangle.save_to_file([r1, r2])
            list_rectangles_output = Rectangle.load_from_file()
            self.assertEqual(str(r1), str(list_rectangles_output[0]))


if __name__ == "__main__":
    # if it is run directly
    unittest.main()
