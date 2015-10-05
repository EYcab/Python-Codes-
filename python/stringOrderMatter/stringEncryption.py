#!/usr/bin/env python
import string, sys
from string import maketrans   # Required to call maketrans function.


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    K = int(sys.stdin.readline())
    K = K%26
    #list out all the chars in ascii_ order
    chars = string.ascii_lowercase
    #print charsOrder in lowercase's case 
    cipher = chars[K:] + chars[:K]
    
    #print cipher + cipher.upper()
    #trantab = maketrans(intab, outtab)
    #translate script is to direct translation from the intab to the outtab
    transcript=maketrans(chars + chars.upper(), cipher + cipher.upper())
    print(S.translate(transcript))