#!/usr/bin/python3
"""  Python script that takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


def status():
    """URL"""
    if len(sys.argv) == 1:
        l = ""
    else:
        l = sys.argv[1]

    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': l})

    try:
        if len(res.json()) == 0:
            print('No result')
        else:
            print('[{}] '.format(res.json()['id']), end='')
            print(res.json()['name'])
    except:
        print('Not a valid  JSON')

if __name__ == '__main__':
    status()
