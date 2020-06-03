#!/usr/bin/python3
"""Can I? Yes, I can"""


def add_attribute(obj, name, value):
    try:
        setattr(obj, name, value)
    except:
        raise TypeError('can\'t add new attribute')
