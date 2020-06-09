#!/usr/bin/python3
"""
Test
"""
import unittest
from models.base import Base


class test_Base(unittest.TestCase):
    """
    class test full
    """
    def test_1(self):
        """1"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
