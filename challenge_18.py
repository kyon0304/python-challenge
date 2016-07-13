# gives http://www.pythonchallenge.com/pc/hex/bin.html with un: butter pw: fly
#! /usr/bin/env python

# from PIL import Image
#
# def minus(t1, t2):
#     ans = []
#     for i in range(len(t1)):
#         ans.append(t1[i] - t2[i])
#     print(t1, t2, ans)
#     return tuple(ans)
#
# if __name__ == '__main__':
#     im = Image.open('balloons.jpg')
#     x, y = im.size
#     x = x // 2
#     diff_im = Image.new(im.mode, (x, y))
#     for j in range(1):
#         for i in range(x):
#             diff = minus(im.getpixel((i, j)), im.getpixel((i+x, j)))
#             diff_im.putpixel((i, j), diff)
#
#     diff_im.save('diff.jpg')
    # print(im.mode)

#==========it is just the brightness, and get a deltas.gz file to work on=======

import gzip
import difflib
# import png
# from PIL import Image

# if __name__ == '__main__':
#     left, right = [], []
#     d = difflib.Differ()
#     wf = open('diff', 'w')
#     with gzip.open('deltas.gz', 'r') as f:
#         data = f.readline()
#         while data:
#             d1 = (data[:53] + b'\n').decode('utf-8')
#             d2 = data[56:].decode('utf-8')
#             # if len(d1)>1:
#             left.append(d1)
#             right.append(d2)
#             data = f.readline()
#     wf.write(''.join(d.compare(left, right)))
#     wf.close()
#
#     # p1, p2, p3 = [], [], []
#     p = [[], [], []]
#     with open('diff', 'r') as f:
#         data = f.readline()
#         # print(data[0] ==' ')
#         while data:
#             # num = [int(i, 16) for i in data[2:].strip().split()]
#             # num = data[2:].strip().encode('utf-8')
#             num = ' '.join([str(int(i, 16)) for i in data[2:].strip().split()]).encode('utf-8')
#             prefix = data[0]
#             data = f.readline()
#             if len(num) == 0:
#                 continue
#             if prefix == ' ':
#                 p[0].append(num)
#             elif prefix == '-':
#                 p[1].append(num)
#             elif prefix == '+':
#                 p[2].append(num)
#             # else:  #the space line
#             #     print('What?', data[0])
#     # print(len(p[0]), len(p[1]), len(p[2]))
#     # print([hex(i)[2:] for i in p[0][0][:10]])
#     # print([hex(i)[2:] for i in p[1][0][:10]])
#     # print([hex(i)[2:] for i in p[2][0][:10]])
#     # print(p[1][:10])
#     # print(p[2][:10])
#     for i in range(3):
#         with open(str(i+1)+'.png', 'wb') as f:
#             # w = png.Writer(54, len(p[i]))
#             # w.write(f, p[i])
#             f.write(b' '.join(p[i]))
#             # data = ''.join(p[i]).encode('utf-8')
#             # f.write(data)

#===============================================================================

if __name__ == '__main__':
    gzf = gzip.open('deltas.gz')
    part_1, part_2 = [], []
    for line in gzf:
        part_1.append(line[:53])
        part_2.append(line[56:-1])
    gzf.close()
    print('part_1', part_1[:10])
    d = difflib.Differ()
    p = [[], [], []]
    for diff in list(d.compare(part_1, part_2)):
        # print(diff)
        num = [int(c, 16) for c in eval(diff[2:]).strip().split(b' ') if c]
        if len(num) == 0:
            continue
        if diff[0] == ' ':
            p[0].append(num)
        elif diff[0] == '-':
            p[1].append(num)
        elif diff[0] == '+':
            p[2].append(num)
    print('p0[0]', p[0][0], bytes(p[0][0]))
    for i in range(3):
        with open('delta%d.png' % i, 'wb') as f:
            # f.writelines(p[i])
            data = []
            for row in p[i]:
                # print(bytes(row))
                data.append(bytes(row))
            # print(p[i])
            print('data', data[0])
            f.writelines(data)
            # f.write(p[i])
