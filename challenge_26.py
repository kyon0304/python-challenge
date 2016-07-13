#gives http://www.pythonchallenge.com/pc/hex/speedboat.html
#/usr/bin/env python

import hashlib

if __name__ == '__main__':
    with open('mybroken.zip', 'rb') as f:
        broken = f.read()

    for i in range(len(broken)):
        for j in range(256):
            repaired = broken[:i] + bytes([j]) + broken[i+1:]
            if hashlib.md5(repaired).hexdigest() == 'bbb8b499a0eef99b52c7f13f4e78c24b':
                with open('mybroken.zip', 'wb') as f:
                    f.write(repaired)
                    # f.save()
                print(i, j)
                raise StopIteration
