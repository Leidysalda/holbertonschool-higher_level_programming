#!/usr/bin/python
"""test square"""
import unittest
from models.base import Base
from models.square import Square


class test_square(unittest.TestCase):
    """test square"""
    def test_square(self):
        """test_1"""
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
