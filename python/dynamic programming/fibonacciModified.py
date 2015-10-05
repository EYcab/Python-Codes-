#!/usr/bin/env python
import sys
if __name__ == '__main__':
    A, B, N = list(map(int, sys.stdin.readline().split()))
    N -=2
    while N>0:
        C=B
        B=B**2+A
        A=C
        N-=1        
    print(B)


#Notice the switch variable process