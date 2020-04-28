#!/usr/bin/python3
for n in range(100):
    o = n / 10
    p = n % 10

    if o < p and 0 != p and n != 89:
        print("{:02d}".format(n), end=',')
    elif n == 89:
        print("{:02d}".format(n))
