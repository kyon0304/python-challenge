#gives http://www.pythonchallenge.com/pc/hex/ambiguity.html
#! /usr/bin/env

from string import ascii_lowercase

def rot13(s):
    intab = ascii_lowercase
    outtab = intab[13:] + intab[:13]
    trans = str.maketrans(intab, outtab)
    return s.translate(trans)

if __name__ == '__main__':
    hint = 'va gur snpr bs jung'
    print("%s:\n" % rot13(hint))
    import this
