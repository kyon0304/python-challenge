# gives http://www.pythonchallenge.com/pc/ring/grandpa.html
# then http://www.pythonchallenge.com/pc/rock/grandpa.html with un:kohsamui pw: thailand
#! /usr/bin/env python

import csv
from PIL import Image

if __name__ == '__main__':
    with open('yankeedoodle.csv', 'r') as f:
        reader = csv.reader(f)
        row_data = []
        for row in reader:
            for d in row:
                row_data.extend(d.split())
    length = len(row_data)
    for i in range(1, 100):
        if length % i == 0:
            w = length // i
            h = i

    data = [float(d) for d in row_data]
    # print(data[:20])
    im = Image.new('P', (w, h))
    i = 0
    for x in range(w):
        for y in range(h):
            d = int(data[i] * 256)
            im.putpixel((x, y), d)
            i += 1

    im.show()
    im.save('yankee.png')

    exc = []
    i = 0
    for i in range(0, len(data), 3):
        try:
            ans.append(row_data[i][5] + row_data[i+1][5] + row_data[i+2][6])
        except:
            pass

    ans = ''.join([chr(int(d)) for d in ans])
    print(ans)
