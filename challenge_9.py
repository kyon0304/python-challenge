# from http://www.pythonchallenge.com/pc/return/good.html
# gives http://www.pythonchallenge.com/pc/return/bull.html
#! /usr/bin/env python
from PIL import Image

def read_file(fn):
    first = second = ''
    with open(fn) as f:
        while 1:
            data = f.readline()
            if data == 'second:\n':
                break
            first += data
        while data:
            data = f.readline()
            second += data
    a1 = list(map(int, first.split(',')))
    a2 = list(map(int, second.split(',')))
    return a1, a2

def dot_on_img(im, l, fn):
    pix = im.load()
    coord = zip(l[::2], l[1::2])
    for i, j in coord:
        pix[i-1, j-1] = (0, 0, 0)
        pix[i, j-1] = (0, 0, 0)
        pix[i+1, j-1] = (0, 0, 0)
        pix[i-1, j] = (0, 0, 0)
        pix[i, j] = (0, 0, 0)
        pix[i+1, j] = (0, 0, 0)
        pix[i-1, j+1] = (0, 0, 0)
        pix[i, j+1] = (0, 0, 0)
        pix[i+1, j+1] = (0, 0, 0)

    im.save(fn)

if __name__ == '__main__':
    im = Image.open("good.jpg")
    px = im.load()
    print(im.size)
    first, second = read_file('connect_the_dots')
    print(len(first), len(second))
    print(im.mode)
    dot_on_img(im, first, "first.jpg")
    dot_on_img(Image.open('first.jpg'), second, 'second.jpg')
