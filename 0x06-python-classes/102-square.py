#!/usr/bin/python3
"""My first square"""


class Square:
    """Class define a square"""

    def __init__(self, size=0):
        """init"""
        self.__size = size

    @property
    def size(self):
        """Retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """Use setter"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Instance that return current square area"""
        return self.__size ** 2

    def equal(self, ot):
        """equal"""
        return self.size == ot.size

    def diferent(self, val):
        """diferente"""
        return self.size != ot.size

    def may(self, val):
        """mayor"""
        return self.size > ot.size

    def may_eq(self, val):
        """mayor equal"""
        return self.size >= ot.size

    def menor(self, val):
        """menor"""
        return self.size < ot.size

    def menorEqual(self, val):
        """menor equal"""
        return self.size <= ot.size
