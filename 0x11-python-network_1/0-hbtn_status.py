#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status
import urllib.request


def fetch():
    """URL"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        ret = response.read()
        uft = ret.decode('utf-8')
        print('Body response:')
        print('    - type: {}'.format(type(ret)))
        print('    - content: {}'.format(ret))
        print('    - utf8 content: {}'.format(uft))

        
if __name__ == '__main__':
    fetch()
