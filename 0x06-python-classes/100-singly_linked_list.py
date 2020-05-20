#!/usr/bin/python3


class Node:
    """Class defines a node of a singly linked list """

    def __init__(self, data, next_node=None):
        """init"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data property"""
        return self.data

    @data.setter
    def data(self, value):
        """data setter"""
        if type(data) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = data

    @property
    def next_node(self):
        """new instance node"""
        return self.next_node

    @next_node.setter
    def next_node(self, value):
        """setter"""
        if type(value) is None or value is None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """defines a single linked list"""

    def __init__(self):
        """init"""
        self.__head = None

    def sorted_insert(self, value):
