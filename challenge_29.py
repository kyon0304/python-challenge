# gives http://www.pythonchallenge.com/pc/ring/yankeedoodle.html
#! /usr/bin/env python

import bz2
if __name__ == '__main__':
    with open('silence_29.html', 'r') as f:
        d = f.readline()
        data = []
        while d:
            if d.strip():
                d = f.readline()
                continue
            data.append(len(d) - 1)
            d = f.readline()
    print(bytes(data))

    bz = bz2.BZ2Decompressor().decompress(bytes(data)).decode('utf-8')
    print(bz)
