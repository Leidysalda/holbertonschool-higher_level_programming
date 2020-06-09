#!/usr/bin/python3
"""Base class"""
import json
import turtle


class Base:
    """First class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        self.id = id

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ sharing data representation"""
        if list_dictionaries:
            dict = json.dumps(list_dictionaries)
            return(dict)
        return('[]')

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        new = []
        open_name = cls.__name__ + '.json'
        if list_objs is not None:
            for obj in list_objs:
                new.append(obj.to_dictionary())

        with open(open_name, 'w') as file:
            file.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is not None:
            list = json.loads(json_string)
            return list
        return('[]')

    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        bob = turtle.Turtle

        bob.pos(0)
        bob.left(list_squares)
        bob.forward(100)

        turtle.done()
