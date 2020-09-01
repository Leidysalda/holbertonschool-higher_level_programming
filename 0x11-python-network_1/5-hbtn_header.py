#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and
 displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys


def status():
    """URL"""
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))


if __name__ == '__main__':
    status()
