#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays the body of the response.
"""
import requests
import sys


def status():
    """URL"""
    try:
        res = requests.get(sys.argv[1])
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.HTTPError as err:
        print('Error code: {}'.format(res.status_code))
        
    
if __name__ == '__main__':
    status()
