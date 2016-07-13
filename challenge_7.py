#gives http://www.pythonchallenge.com/pc/def/integrity.html
#! /usr/bin/env python

from PIL import Image
import re

def img_guess(px, a):
    data =[]
    for i in a:
        current = px[i, 47]
        if current[0] == current[1] == current[2]:
            current = current[0]
            data.append(current)
    ans = ''.join([chr(i) for i in data])

    return ans

if __name__ == '__main__':
    im = Image.open('oxygen.png')
    px = im.load()
    x, y = im.size
    hint = img_guess(px, range(0, x-1, 7))
    print(hint)
    print('answer is:', ''.join(map(chr, map(int, re.findall('\d+', hint)))))
