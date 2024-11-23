#!/usr/bin/python3
"""Unittest for Base
"""
import unittest
from models.rectangle import Rectangle


class TestMaxInteger(unittest.TestCase):
    def test_two_arguments(self):
        b1 = Rectangle(1, 2)
        self.assertEqual(b1.width, 1)
        self.assertEqual(b1.height, 2)
        self.assertEqual(b1.x, 0)
        self.assertEqual(b1.x, 0)

    def test_three_arguments(self):
        b2 = Rectangle(1, 2, 3)
        self.assertEqual(b2.x, 3)
        self.assertEqual(b2.y, 0)

    def test_four_arguments(self):
        b2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(b2.x, 3)
        self.assertEqual(b2.y, 4)
        
if __name__ == '__main__':
    unittest.main()