# gives http://www.pythonchallenge.com/pc/return/cat.html
# and then http://www.pythonchallenge.com/pc/return/uzi.html
#! /usr/bin/env python

from PIL import Image

def get_data(fn):
    im = Image.open(fn)
    px = im.load()
    # print(im.mode)
    return px

def conv(data):
    w = 100
    h = 100
    rd = 0
    n = 0
    im = Image.new('RGB', (100, 100), 0)
    px = im.load()
    while 1:
        for i in range(rd, w-rd):
            px[i, rd] = data[n, 0] #top
            n += 1
        for i in range(rd+1, h-rd):
            px[w-1-rd, i] = data[n, 0] #right
            n += 1
        for i in range(w-rd-2, rd-1, -1):
            px[i, h-1-rd] = data[n, 0] #bottom
            n += 1
        for i in range(h-rd-2, rd, -1):
            px[rd, i] = data[n, 0] #left
            n += 1
        rd += 1
        if rd == 50:
            break
    print('save to wired.png')
    im.save('wired.png')

def tashan(fn):
    im = Image.open(fn)
    wired = Image.new(im.mode, (100, 100), 0)
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    x, y, z = -1, 0, 0
    for i in range(200):
        d = dirs[i % 4]
        for j in range(100 - (i + 1) // 2):
            x += d[0]
            y += d[1]
            wired.putpixel((x,y), im.getpixel((z, 0)))
            z += 1
    print('save to wired.png')
    wired.save('wired.png')


if __name__ == '__main__':
    # data = get_data('wire.png')
    # conv(data)
    tashan('wire.png')
