__author__ = 'Chenxi'
# a Brute force approach

import sys
if sys.version_info[0]>=3: raw_input=input
N = int(raw_input())
for n in range(0,N):
    T = int(raw_input())
    cubes = list(int(x) for x in raw_input().replace("\r","").strip().split(" "))
    i = 0
    j = len(cubes)-1
    cur = max(cubes[i],cubes[j])
    ANS = "Yes"

    while j-i > -1:
        if cubes[i] > cubes[j]:
            nex = cubes[i]
            i += 1
        else:
            nex = cubes[j]
            j -= 1

        if nex > cur:
            ANS = "No"
            break
        cur = nex

    print(ANS)



