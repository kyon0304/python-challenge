# gives http://www.pythonchallenge.com/pc/return/5808.html
#! /usr/bin/env python

def merge_list(l, m):
    data = []
    for i in range(len(l)):
        data.append(l[i])
        data.append(m[i])
    return data

def cnt_num(l, recursed_cnt):
    data = []
    cnt = []
    for i in l:
        if len(data) > 0:
            if data[-1] == i:
                cnt[-1] += 1
            else:
                data.append(i)
                cnt.append(1)
        else:
            data.append(i)
            cnt.append(1)

    merged = merge_list(cnt, data)
    if recursed_cnt == 29:
        size = len(merged)
        print(size)
        return
    else:
        cnt_num(merged, recursed_cnt + 1)

if __name__ == '__main__':
    cnt_num([1], 0)
