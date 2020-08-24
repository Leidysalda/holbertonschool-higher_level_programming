#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and
 displays the value of the X-Request-Id variable found in the header of
 the response
"""
import urllib.request
import sys


def status():
    """URL"""
    head = {'X-Request-Id'}
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        print(response.info()['X-Request-Id'])


if __name__ == '__main__':
    status()
