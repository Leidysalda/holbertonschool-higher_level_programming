#!/usr/bin/python3
"""Test rectangle"""
import unittest
from models.base import Base


class test_Rectangle(unittest.TestCase):
    """Test Rectangle"""

    def test_create_rectangle(self):
        """test create"""
        b1 = base()
        self.assertEqual(b1.id, 1)
