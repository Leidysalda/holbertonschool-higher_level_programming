#!/usr/bin/python3
"""Can I?"""


def add_attribute(obj, name, value):
    """ Method add """
    try:
        setattr(obj, name, value)
    except:
        raise TypeError('can\'t add new attribute')
