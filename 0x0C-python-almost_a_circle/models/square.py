#!/usr/bin/python3
"""The square"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)
        self.__width = size

    def __str__(self):
        """str"""
        return('[Square] ({}) {}/{} - {}'
               .format(self.id, self.x, self.y, self.__width))

    @property
    def size(self):
        """private instance size"""
        return self.__width

    @size.setter
    def size(self, value):
        """private instance"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value
            self.__height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.__width = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        dict = {
            'id' : self.id,
            'size' : self.__width,
            'x' : self.x,
            'y' : self.y
        }
        return(dict)
