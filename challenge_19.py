#gives http://www.pythonchallenge.com/pc/hex/idiot.html
#! /usr/bin/env python

import base64
import wave
import codecs
# import requests

def my_hex(s):
    return codecs.getencoder('hex')(s)[0]

if __name__ == '__main__':
#=====================decode the attachment ====================================
    # with open('attach_19', 'r') as f:
    #     attachment = f.read()
    #
    # data = base64.b64decode(attachment)

    # with open('indian.wav', 'wb') as f:
    #     f.write(data)

#===============try to send by cookie, do not take effect=======================
    # url = 'http://www.pythonchallenge.com/pc/hex/sorry.html'
    # cookies = dict(info='sorry')
    # r = requests.post(url, cookies, auth=('butter', 'fly'))
    # # with open('resp_19', 'w') as f:
    # #     f.write(r.text)
    # print(r.text)

#=====================manipulate the attachment ================================
    with wave.open('indian.wav', 'rb') as f:
        print(f.getparams())
        fr = f.getframerate()
        sw = f.getsampwidth()
        frames = f.readframes(f.getnframes())
    with wave.open('indian_new.wav', 'wb') as f:
        f.setnchannels(1)
        f.setsampwidth(sw)
        f.setframerate(fr//2)
        f.writeframes(frames[::2])
