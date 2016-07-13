#google and gives http://www.pythonchallenge.com/pc/rock/arecibo.html
# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np

def iter_point(c):
    z = 0
    for i in range(128): # 最多迭代128次
        z = z*z+c
        if abs(z)>2: break # 半径大于2则认为逃逸
    return i # 返回迭代次数

#===================ta shan ====================================================

def solve():
    x = 0.34
    y = 0.57
    w = 0.036
    h = 0.027

    im = Image.open('mandelbrot.gif')
    imdata = np.array(list(im.getdata()))
    im_w, im_h = im.size
    dw = w / im_w
    dh = h / im_h
    xx = np.linspace(x, x+w-dw, im_w)
    yy = np.linspace(y, y+h-dh, im_h)
    yy = yy[::-1]
    xx.shape = (1, im_w)
    yy.shape = (im_h, 1)
    grids = xx + 1j * yy

    for i in range(im_h):
        for j in range(im_w):
            grids[i, j] = iter_point(grids[i, j])

    grids.reshape((-1,))
    im.putdata(grids.reshape((-1,)))
    im.show()

    imdata.shape = (480, 640)
    diffs = imdata - grids
    msg = diffs[np.where(np.abs(diffs) == 16)]

    newIm = Image.new('1', [23, 73])
    newIm.putdata([255 if i > 0 else 0 for i in msg])
    newIm.show()
    newIm.save('level31_out.png')

if __name__ == '__main__':
    solve()
