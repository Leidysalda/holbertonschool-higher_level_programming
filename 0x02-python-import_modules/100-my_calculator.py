#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

try:
    if len(argv) == 4:
        a = (int(argv[1]))
        b = (int(argv[3]))
        if argv[2] == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif argv[2] == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif argv[2] == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif argv[2] == '/':
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

except Exception as e:
    pass
