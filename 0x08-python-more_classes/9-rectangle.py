#!/usr/bin/python3
"""More classes and objects"""


class Rectangle:
    """class rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """returns the rectangle area"""
        return self.height * self.width

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.width == 0 and self.height == 0:
            return 0
        else:
            return(2 * (self.width + self.height))

    def __str__(self):
        """Method convert to string"""
        if self.width == 0 and self.height == 0:
            return ('')
        else:
            for i in range(self.height):
                for j in range(self.width):
                    print('{}'.format(self.print_symbol), end='')
                if i != self.height - 1:
                    print('')
            return('')

    def __repr__(self):
        """object state"""
        return('Rectangle({}, {})'.format(self.width, self.height))

    def __del__(self):
        """Delete instance"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return(Rectangle(size, size))
