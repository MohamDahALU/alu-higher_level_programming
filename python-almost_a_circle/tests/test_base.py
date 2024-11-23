#!/usr/bin/python3
"""Unittest for Base
"""
import unittest
from models.base import Base


class TestMaxInteger(unittest.TestCase):
    def test_one_instance(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_three_instances(self):
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_with_argument(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

if __name__ == '__main__':
    unittest.main()