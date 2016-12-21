#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Send SMS

2016
Xaratustra

"""

FROM = ""
USER = ""
URL = "https://www.voipcheap.com/myaccount/sendsms.php?username={}&password={}&from={}&to={}&text="

from urllib.request import urlopen
from getpass import getpass
import sys


def send_sms(msg):
    to = input('To:')
    pw = getpass()
    msg = URL.format(USER, pw, FROM, to) + msg
    urlopen(msg).read()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        send_sms(sys.argv[1])
    else:
        print('Please provide a message, inside quotes.')
