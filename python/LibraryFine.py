#!/usr/bin/env python

import sys


if __name__ == '__main__':
    D_actual, M_actual, Y_actual = list(map(int, sys.stdin.readline().split()))
    D_expected, M_expected, Y_expected = list(map(int, sys.stdin.readline().split()))
    
    #attention to this series of codes
    if Y_actual < Y_expected or (Y_actual == Y_expected and M_actual < M_expected) or (Y_actual == Y_expected and M_actual == M_expected and D_actual <= D_expected):
        print(0)
    elif Y_actual == Y_expected and M_actual == M_expected:
        print(15 * (D_actual - D_expected))
    elif Y_actual == Y_expected:
        print(500 * (M_actual - M_expected))
    else:
        print(10000)

