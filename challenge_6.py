#! /usr/bin/env python
# get zipped file from "http://www.pythonchallenge.com/pc/def/channel.zip"
# gives http://www.pythonchallenge.com/pc/def/oxygen.html

import zipfile

def z():
    zf = zipfile.ZipFile('channel.zip', 'r')
    # print(zf.read('readme.txt').decode('utf-8'))

    content = zf.read('90052.txt').decode('utf-8')
    fn = content.split()[-1] + '.txt'
    # print(content)
    print(zf.getinfo('90052.txt').comment.decode('utf-8'), end='')

    count = 0
    while count < len(zf.namelist()) - 3:
        content = zf.read(fn).decode('utf-8')
        fn = content.split()[-1] + '.txt'
        # print(content)
        print(zf.getinfo(fn).comment.decode('utf-8'), end='')
        count += 1

if __name__ == '__main__':
    z()
