#!/usr/bin/env python
#from easy Sum in 
import sys


if __name__ == '__main__':
    testCases = int(sys.stdin.readline())
    
    triangular_num = lambda n: n * (n + 1) // 2
    
    for _ in range(testCases):
        N, m = list(map(int, sys.stdin.readline().split()))
        print((N // m) * triangular_num(m - 1) + triangular_num(N % m))