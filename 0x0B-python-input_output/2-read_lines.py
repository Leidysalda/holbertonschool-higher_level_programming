#!/usr/bin/env python3
"""Read n lines"""


def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a text file (UTF8) and prints"""
    with open(filename, 'r') as file:
        if nb_lines > 0 and nb_lines:
            for i in range(nb_lines):
                a = file.readline()
                print(a, end='')
        else:
            a = file.read()
            print(a, end='')
