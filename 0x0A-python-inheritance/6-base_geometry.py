#!/usr/bin/python3


class BaseGeometry:
    """Class Base"""

    def __dir__(self):
        """function __dir__ """
        obj = BaseGeometry
        return dir(obj)

    def area(self):
        raise Exception('area() is not implemented')
