#!/usr/bin/python
from urllib import urlencode
import urllib2
import time
import argparse
# change the these to your BT account email address
BT_LOGIN = None
PASSWORD = None
SLEEP = 40


def login():
    print('Logging you into BTWifi...')
    url = 'https://www.btopenzone.com:8443/tbbLogon'
    if BT_LOGIN is None or PASSWORD is None:
        raise ValueError('You must specify your login email and password')
    data = {
        'username': BT_LOGIN,
        'password': PASSWORD
    }
    req = urllib2.Request(url, urlencode(data), {})
    resp = urllib2.urlopen(req)

    if '/accountLogoff' in resp.read():
        return True
    else:
        return False


def main():
    try:
        # using google hosted small webpage to test
        # our requests aren't being moved to BT
        urllib2.urlopen('http://www.google.com/iwanta404page')
        if login() is False:
            print('Login failed')
    except (urllib2.HTTPError, urllib2.URLError):
        # Wifi should be working
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', help='Your BT login email')
    parser.add_argument('--password', help='Your BT login password')
    args = parser.parse_args()
    BT_LOGIN = args.email
    PASSWORD = args.password
    while True:
        main()
        print('sleeping for {} seconds...'.format(SLEEP))
        time.sleep(SLEEP)
