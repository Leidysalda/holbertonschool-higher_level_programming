#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request
 to the passed URL with the email as a parameter, and displays the body
 of the response (decoded in utf-8)
"""
import urllib.request
import sys
import urllib.parse


def status():
    """URL"""
    value = {'email' : sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
    print('Your email is: {}'.format(sys.argv[2]))


if __name__ == '__main__':
    status()
