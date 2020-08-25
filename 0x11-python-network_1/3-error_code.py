#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request
 to the passed URL with the email as a parameter, and displays the body
 of the response (decoded in utf-8)
"""
import urllib.request
import sys
import urllib.error


def status():
    """URL"""
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            page = response.read()
            print(page.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))


if __name__ == '__main__':
    status()
