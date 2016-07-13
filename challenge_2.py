# gives http://www.pythonchallenge.com/pc/def/equality.html

#! /usr/bin/env python

from string import ascii_lowercase

def rare(s):
    ans = ''
    for c in s:
        if c in ascii_lowercase:
            ans += c
    return ans

if __name__ == '__main__':
    clue = ''
    with open("challenge_2_clue") as f:
        clue = f.read()
    print(rare(clue))
