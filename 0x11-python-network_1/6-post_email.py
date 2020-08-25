#!/usr/bin/python3
""" Python script that takes in a URL and an email address, sends a
 POST request to the passed URL with the email as a parameter, and
 finally displays the body of the response.
"""
import requests
import sys


def status():
    """URL"""
    data = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data)
    print(res.text)


if __name__ == '__main__':
    status()
