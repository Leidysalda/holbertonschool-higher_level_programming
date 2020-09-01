#!/usr/bin/python3
"""  Python script that takes your Github credentials (username and password)
 and uses the Github API to display your id
"""
import requests
import sys


if __name__ == '__main__':

    url = "https://api.github.com/repos/{}/{}/commits"
    .format(sys.argv[1], sys.argv[2])

    res = requests.get(url)

    try:
        print(res.json()['id'])
    except KeyError:
        print('None')
