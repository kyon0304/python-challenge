# gives http://www.pythonchallenge.com/pc/ring/guido.html
# python creator Guido van Rossum
#! /usr/bin/env python

from PIL import Image

if __name__ == '__main__':
    im = Image.open('bell.png')
    w, h = im.size
    # print(w)

    g = list(im.getdata(1)) #get green band

    differ = []
    evenG = g[::2]
    oddG = g[1::2]
    data = zip(evenG, oddG)
    # differ = list(lambda d: d[0] - d[1] for d in data)
    for d in data:
        differ.append(d[0]-d[1])

    distinct = []
    for i, d in enumerate(differ):
        if d != 42 and d != -42:
            distinct.append((i, d))

    coordinate = []
    ans = []
    for d in distinct:
        x = d[0] % w
        y = d[0] // w
        coordinate.append((x, y, d[1]))

    print(coordinate)

    ans = [chr(abs(i[1])) for i in distinct]

    print(''.join(ans))
