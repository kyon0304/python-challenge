# gives http://www.pythonchallenge.com/pc/def/peak.html
#! /usr/bin/env python

from urllib import request
import sys
import signal

def signal_handler(signal, frame):
    print("You pressed ctrl-c!")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def linker():
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    suffix = '12345'
    count = 0
    print("get enconding method...")
    codec = request.urlopen(url + suffix).headers.get_content_charset()
    print("and it's:", codec)
    while count < 400:
        resp = request.urlopen(url + suffix)
        suffix = resp.read().decode(codec).split()[-1]
        print("round %d suffix: %s" % (count, suffix))
        count = count + 1

if __name__ == '__main__':
    linker()
