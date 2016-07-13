# gives {'switch', '../ring/bell.html', 'repeat', 'exec', 'print'}
# goes to http://www.pythonchallenge.com/pc/ring/bell.html with un:repeat and pw:switch
#! /usr/bin/env python

from PIL import Image
import bz2
import keyword

if __name__ == '__main__':
    im = Image.open('zigzag.gif')

    pd = list(im.getdata())
    pp = im.getpalette()[::3]
    rc = [pp[i] for i in pd]
    pd = pd[1:] + pd[:1]

    d = []
    for i, p in enumerate(pd):
        if rc[i] != p:
            d.append(p)
    bz = bz2.BZ2Decompressor().decompress(bytes(d)).decode('utf-8').split()
    # print(keyword.kwlist)
    ans = [i for i in bz if i not in keyword.kwlist]
    print(set(ans))
