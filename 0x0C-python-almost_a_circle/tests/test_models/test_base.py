#!/usr/bin/python3
"""
Test
"""
import unittest
import pep8


class test_Base(unittest.TestCase):
    """
    class test full
    """
    def test_pep8_conformance(self):
        """
        Test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'models/rectangle.py'
                                        'models/square.py'])

        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
