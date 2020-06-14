#!/usr/bin/python3
"""
Test
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Base(unittest.TestCase):
    """
    class test full
    """
    def test_1(self):
        """1"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(8)
        self.assertEqual(b2.id, 8)
        b3 = Base('a')
        self.assertEqual(b3.id, 'a')
        b4 = Base(89)
        self.assertEqual(b4.id, 89)
