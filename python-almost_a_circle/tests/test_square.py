#!/usr/bin/python3
"""Unittest for Base
"""
import unittest
from models.square import Square
import io
import sys


class TestMaxInteger(unittest.TestCase):
    def test_square_one_arg(self):
        obj = Square(1)
        self.assertEqual(obj.size, 1)

    def test_square_two_arg(self):
        obj = Square(1, 2)
        self.assertEqual(obj.x, 2)

    def test_square_three_arg(self):
        obj = Square(1, 2, 3)
        self.assertEqual(obj.y, 3)

    def test_square_four_arg(self):
        obj = Square(1, 2, 3, 4)
        self.assertEqual(obj.id, 4)
    
    def test_square_one_arg_string(self):
        with self.assertRaises(TypeError) as err:
            Square("1")
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_square_two_arg_string(self):
        with self.assertRaises(TypeError) as err:
            Square(1, "2")
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_square_three_arg_string(self):
        with self.assertRaises(TypeError) as err:
            Square(1, 2, "3")
        self.assertEqual(str(err.exception), "y must be an integer")
    
    def test_square_one_arg_negative(self):
        with self.assertRaises(ValueError) as err:
            Square(0)
        self.assertEqual(str(err.exception), "width must be > 0")
        
    def test_square_one_arg_negative(self):
        with self.assertRaises(ValueError) as err:
            Square(-1)
        self.assertEqual(str(err.exception), "width must be > 0")
    
    def test_square_two_arg_negative(self):
        with self.assertRaises(ValueError) as err:
            Square(1, -2)
        self.assertEqual(str(err.exception), "x must be >= 0")
    
    def test_square_three_arg_negative(self):
        with self.assertRaises(ValueError) as err:
            Square(1, 2, -3)
        self.assertEqual(str(err.exception), "y must be >= 0")

if __name__ == '__main__':
    unittest.main()