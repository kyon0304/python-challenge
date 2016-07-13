# gives http://www.pythonchallenge.com/pc/def/linkedlist.php
#! /usr/bin/env python

import re

def re_find(s):
    pattern = re.compile('[^A-Z][A-Z]{3}[a-z]{1}[A-Z]{3}[^A-Z]')
    return pattern.findall(s)

if __name__ == '__main__':
    clue = ''
    with open("challenge_3_clue") as f:
        clue = f.read()
    candi = re_find(clue)
    print(candi)
    ans = ''
    for i in candi:
        ans += i[4]
    print(ans)
