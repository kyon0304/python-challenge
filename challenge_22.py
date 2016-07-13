#!/usr/bin/env python

from PIL import Image

def move_to(path, src):
    x = path[0] - 100
    y = path[1] - 100
    return (src[0] + x, src[1] + y)

if __name__ == '__main__':
    im = Image.open('white.gif')
    px = im.load()
    print(im.info)
    # print(px.__doc__)
    move = []
    try:
        while True:
            for x in range(200):
                for y in range(200):
                    if im.getpixel((x, y)) != 0:
                        move.append((x, y))
                        # print((x, y), im.getpixel((x, y)))
            im.seek(im.tell() + 1)
    except EOFError:
        pass

    joy = Image.new(im.mode, (200, 200), 0)
    letter = 0
    pos = (0, 100)
    last = (0, 100)
    for p in move:
        if p == (100, 100):
            # print('new letter')
            letter += 1
            pos = (letter * 38, 80)
        else:
            pos = move_to(p, last)
            # print(pos)
        last = pos
        joy.putpixel(pos, 255)

    joy.save('joystick.gif')
            # print(im.getpix)
    # print(im.getpixel((100,100)))
