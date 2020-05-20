#!/usr/bin/python3
"""My first square"""


class Square:
    """Class define a square"""
    def __init__(self, size=0):
        """init"""
        self.size = size

    @property
    def size(self):
        """Retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """Use setter"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Instance that return current square area"""
        return self.size ** 2

    def __eq__(self, other):
        """equal"""
        return self.size == other.size

    def __ne__(self, other):
        """diferente"""
        return self.size != other.size

    def __gt__(self, other):
        """mayor"""
        return self.size > other.size

    def __ge__(self, other):
        """mayor equal"""
        return self.size >= other.size

    def __lt__(self, other):
        """menor"""
        return self.size < other.size

    def __le__(self, other):
        """menor equal"""
        return self.size <= other.size
