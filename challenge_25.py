#gives http://www.pythonchallenge.com/pc/hex/decent.html
#! /usr/bin/env python

import wave
from PIL import Image
import base64
from http.client import HTTPConnection

def get_waves():
    unpw = base64.b64encode(b'butter:fly').decode('utf-8')
    header = {'Authorization': 'Basic %s' % unpw}
    conn = HTTPConnection('www.pythonchallenge.com')
    for i in range(1, 27):
        uri = '/pc/hex/lake%d.wav' % i
        conn.request('GET', uri, headers=header)
        resp = conn.getresponse()
        if resp.status == 200:
            with open('lakewave/wave%d.wav' % i, 'wb') as f:
                f.write(resp.read())


if __name__ == '__main__':
    # get_waves()

    im = Image.new('RGB', (300, 300))

    for i in range(25):
        with wave.open('lakewave/wave%d.wav' % (i+1), 'rb') as f:
            data = f.readframes(f.getnframes())
        r = data[::3]
        g = data[1::3]
        b = data[2::3]

        rgb = zip(r, g, b)
        base_x = (i * 60 % 300)
        base_y = (i * 60 // 300) * 60
        c = 0
        x, y = base_x, base_y
        for p in rgb:
            im.putpixel((x, y), p)
            c += 1
            x = base_x + c % 60
            y = base_y + c // 60

    im.save('lakewave/jigsaw.png')
