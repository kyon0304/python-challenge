#gives http://www.pythonchallenge.com/pc/hex/copper.html
#!/usr/bin/env python

import zlib
import bz2

if __name__ == '__main__':
    with open('unreal/package.pack', 'rb') as f:
        content = f.read()

    output = []
    while True:
        if content.startswith(b'BZh'):
            data = bz2.decompress(content)
            output.append('#')
        elif content.startswith(b'x\x9c'):
            data = zlib.decompress(content)
            output.append(' ')
        elif content.endswith(b'\x9cx'):
            data = content[::-1]
            output.append('\n')
        else:
            break
        content = data
    print(''.join(output))
