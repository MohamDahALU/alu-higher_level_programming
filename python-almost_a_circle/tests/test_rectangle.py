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

    def test_five_arguments(self):
        b2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(b2.id, 5)

    def test_width_string(self):
        with self.assertRaises(TypeError) as err:
            Rectangle("1", 2)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_height_string(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(1, "2")
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_x_string(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(1, 2, "3")
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_y_string(self):
        with self.assertRaises(TypeError) as err:
            Rectangle(1, 2, 3, "4")
        self.assertEqual(str(err.exception), "y must be an integer")
    
    def test_width_zero(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(0, 2)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_height_zero(self):
        with self.assertRaises(ValueError) as err:
            Rectangle(1, 0)
        self.assertEqual(str(err.exception), "height must be > 0")
    
    def test_area(self):
        obj = Rectangle(2, 2)
        self.assertEqual(obj.area(), 4)
        
    def test_str(self):
        obj = Rectangle(2, 2, 2, 2, 10)
        self.assertEqual(obj.__str__(), "[Rectangle] (10) 2/2 - 2/2")
        
    def test_display_no_xy(self):
        obj = Rectangle(2, 2)
        stri = obj.display()
        self.assertEqual(stri, None)

    def test_display_no_y(self):
        obj = Rectangle(2, 2, 2)
        stri = obj.display()
        self.assertEqual(stri, None)
        
    def test_display(self):
        obj = Rectangle(2, 2, 2, 2)
        stri = obj.display()
        self.assertEqual(stri, None)
        
if __name__ == '__main__':
    unittest.main()