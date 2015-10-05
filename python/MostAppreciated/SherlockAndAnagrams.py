#!/usr/bin/env python

import collections, sys
def solve(datalist):
    n = len(datalist)
    d = collections.defaultdict(int)
    for i in range(n):
        for l in range(1, n-i+1):
            sub = datalist[i: i+l]
            sub.sort()
            d["".join(sub)] += 1
    s = 0
    for v in d.values():
        s += v*(v-1)//2
    return s          

if __name__=="__main__":
	testcases = int(sys.stdin.readline())
	for t in range(testcases):
		lst=list(sys.stdin.readline().strip())
		print(solve(lst))
        
