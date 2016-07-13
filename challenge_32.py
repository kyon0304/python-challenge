#! /usr/bin/env python

def init(D):
    return [['u' for i in range(D)] for j in range(D)]

if __name__ == '__main__':
    dimension = 9
    pad = init(dimension)
    rows = pad
    cols = [[pad[i][j] for i in range(dimension)] for j in range(dimension)]
