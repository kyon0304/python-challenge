#gives http://www.pythonchallenge.com/pc/def/channel.html
#! /usr/bin/env python

from urllib import request
from pickle import loads

url = "http://www.pythonchallenge.com/pc/def/banner.p"

def peak(url):
    bs = request.urlopen(url).read()
    data = loads(bs)
    return data

if __name__ == '__main__':
    l = peak(url)
    for i in l:
        for t in i:
            print(t[0] * t[1], end='')
        print('\n', end='')
