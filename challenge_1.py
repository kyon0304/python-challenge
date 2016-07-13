# gives http://www.pythonchallenge.com/pc/def/ocr.html

#! /usr/bin/env python

from string import maketrans, ascii_lowercase

clue = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

url = 'map'
def conv(s):
    ans = ""
    for c in s:
        if c in ascii_lowercase:
            idx = (ord(c) + 2 - 97) % 26 + 97
            c = str(unichr(idx))
        ans += c
        # print c,

    return ans

def hint_conv(s):
    intab = ascii_lowercase
    outtab = intab[2:]+intab[:2]
    trantab = maketrans(intab, outtab)

    return s.translate(trantab)

if __name__ == '__main__':
    # print conv(clue)
    print hint_conv(url)
