#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status
"""
import requests


def status():
    """URL"""
    res = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))


if __name__ == '__main__':
    status()
