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

if __name__ == '__main__':
    unittest.main()