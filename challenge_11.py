#!/usr/bin/env python
# gives http://www.pythonchallenge.com/pc/return/evil.html

from PIL import Image

def odd_even(px, x, y):
    even = []
    odd = []
    for i in range(0,y,2):
        even.extend(px[m, i] for m in range(0, x, 2))
    for i in range(1, y, 2):
        odd.extend(px[m, i] for m in range(1, x, 2))
    return odd, even

if __name__ == '__main__':
    im = Image.open('cave.jpg')
    mode = im.mode
    x, y = im.size
    px = im.load()
    odd, even = odd_even(px, x, y)
    odd_img = Image.new(mode, (x//2, y//2))
    # even_img = Image.new(mode, (x//2, y//2))
    odd_img.putdata(odd, 1, 0)
    # even_img.putdata(even, 1, 0)
    odd_img.save('odd.jpg')
    # even_img.save('even.jpg')
