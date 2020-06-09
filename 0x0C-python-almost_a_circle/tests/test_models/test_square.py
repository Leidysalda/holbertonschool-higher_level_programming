#!/usr/bin/python3
"""test square"""
import unittest
from models.rectangle import Rectangle

class test_create_Square(unittest.TestCase):
    """test square"""
    b1 = Rectangle()
    self.asserEqual(b1.id, 1)
