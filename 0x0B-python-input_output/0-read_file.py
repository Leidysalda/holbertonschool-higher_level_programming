#!/usr/bin/env python3


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename) as file:
        a = file.read()
        print(a, end='')
