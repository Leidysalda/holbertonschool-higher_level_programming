#!/usr/bin/python3
"""
Test rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class test_Rectangle(unittest.TestCase):
    """
    Test Rectangle
    """

    def test_create_rectangle(self):
        """
        test create
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 2)
