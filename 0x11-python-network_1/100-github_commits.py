#!/usr/bin/python3
"""  Python script that takes your Github credentials (username and password)
 and uses the Github API to display your id
"""
import requests
import sys


if __name__ == '__main__':

    url = "https://api.github.com/user"
    u = sys.argv[1]
    t = sys.argv[2]

    res = requests.get(url, auth=(u, t))

    try:
        print(res.json()['id'])
    except KeyError:
        print('None')
