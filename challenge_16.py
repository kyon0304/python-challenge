#gives http://www.pythonchallenge.com/pc/return/romance.html
#! /usr/bin/env python

from PIL import Image

def straighten(fn):
    im = Image.open(fn)
    print(im.mode, im.size)
    coord = []
    l1 = 429
    for y in range(480):
        row = [im.getpixel((x, y)) for x in range(640)]
        offset = [row.index(x) for x in row if x == 195][0] - l1
        new_row = row[offset:] + row[:offset]
        for x in range(640):
            im.putpixel((x, y), new_row[x])
    im.save('straighten.gif')

if __name__ == '__main__':
    straighten('mozart.gif')
