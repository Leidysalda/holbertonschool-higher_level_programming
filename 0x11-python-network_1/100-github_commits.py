#!/usr/bin/python3
"""  Python script that takes your Github credentials (username and password)
 and uses the Github API to display your id
"""
import requests
import sys


if __name__ == '__main__':

    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[1], sys.argv[2exi])

    res = requests.get(url)
    res_json = res.json()

    for i in res_json()[:10]:
        print(i)
