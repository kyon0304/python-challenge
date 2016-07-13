#! /usr/bin/env python
# gives http://www.pythonchallenge.com/pc/return/disproportional.html

if __name__ == '__main__':
    data = []
    new_data = [[], [], [], [], []]
    with open('evil2.gfx', 'rb') as f:
        data = f.read()
    n = 0
    for i in range(len(data) - 1):
        new_data[n%5].append(data[i])
        n += 1
    for n, elt in enumerate(new_data):
        f = open(str(n), 'wb')
        f.write(bytearray(elt))
        f.close()
