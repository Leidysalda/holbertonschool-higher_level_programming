#!/usr/bin/python3
"""Magic string"""


def magic_string(n=[0]):
    """Magic string"""
    n[0] += 1; return('Holberton, ' * n[0])[0:len('Holberton, ' * n[0]) - 2]
    for i in range(n): print(magic_string())
