# gives http://www.pythonchallenge.com/pc/return/balloons.html
#!/usr/bin/env python

import requests
import bz2
import urllib
import sys
import signal

from xmlrpc.client import ServerProxy, Error

def signal_handler(signal, frame):
    print("You pressed ctrl-c!")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def linker():
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
    suffix = '12345'
    count = 0
    data = []
    while count < 400:
        resp = requests.get(url + suffix)
        suffix = resp.text.split()[-1]
        try:
            cookie = resp.cookies['info']
        except KeyError as e:
            break
        print("round %d suffix: %s, cookie: %s" % (count, suffix, cookie))
        data.append(cookie)
        count = count + 1
    data = ''.join(data)
    return data

if __name__ == '__main__':
    # data = linker()
    # with open('cookies', 'w') as f:
    #     f.write(data)

    #====================got the cookies, now unzip it==========================
    # with open('cookies', 'r') as f:
    #     readdata = f.read().strip()
    # readdata = readdata.replace('+', ' ')
    # readdata = urllib.parse.unquote_to_bytes(readdata)
    # print(bz2.decompress(readdata))

    #====================got hint, now call=====================================
    # server = ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
    # try:
    #     # resp = server.system.listMethods()
    #     resp = server.phone('Leopold')
    #     print(resp)
    # except Error as err:
    #     print(err)

    #====================connected, now leave message===========================
    url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
    cookies = dict(info=urllib.parse.quote_plus('the flowers are on their way'))
    print(cookies)
    try:
        r = requests.post(url, cookies=cookies)
    except Error as e:
        print(e)
    print(r.text)
