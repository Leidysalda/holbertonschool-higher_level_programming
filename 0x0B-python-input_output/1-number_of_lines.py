#!/usr/bin/env python3
"""Number of lines"""


def number_of_lines(filename=""):
    """function that returns the number of lines of a text file"""
    with open(filename) as file:
        return(len(file.readlines()))
