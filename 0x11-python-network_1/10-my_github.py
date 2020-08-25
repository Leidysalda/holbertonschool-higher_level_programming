#!/usr/bin/python3
"""  Python script that takes your Github credentials (username and password)
 and uses the Github API to display your id
"""
import requests
import sys


def status():
    """URL"""
    
    res = requests.get('https://api.github.com/user', auth=(username, passwd))
    datajson = response.json()
    print(datajson.get('id'))


if __name__ == '__main__':
    status()
