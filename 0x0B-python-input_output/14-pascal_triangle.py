#!/usr/bin/python3
import sys


def pascal_triangle(n):
    """pascal"""
    if n == 0:
        return []
    elif n == 1:
        return[[1]]
    else:
        new_r = [1]
        res = pascal_triangle(n - 1)
        last_r = res[-1]
        for i in range(len(last_r)-1):
            new_r.append(last_r[i] + last_r[i + 1])
        new_r += [1]

        res.append(new_r)
    return res
