#!/usr/bin/python3
"""More classes and objects"""


class Rectangle:
    """Empty class """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """private instance width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """private instance height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.height * self.width

    def perimeter(self):
        """Returns the rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return(2 * (self.width + self.height))
