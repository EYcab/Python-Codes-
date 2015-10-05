#!/usr/bin/env python

import string, sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    K = int(sys.stdin.readline())
    K = K%26
    chars = string.ascii_lowercase
    cipher = chars[K:] + chars[:K]
    
    print(S.translate(str.maketrans(chars + chars.upper(), cipher + cipher.upper())))