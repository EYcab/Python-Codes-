#The 1st soln is wrong,since when T>2 or 3+,
#while loop should not be executing as it will cause errors

import sys
def quicksort(lst):
        if len(lst) == 0:
            return []
        else:
            return quicksort([x for x in lst[1:] if x < lst[0]]) + [lst[0]] + \
                   quicksort([x for x in lst[1:] if x >= lst[0]])

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    sticks = list(map(int, sys.stdin.readline().split()))
    sticksSorted = quicksort(sticks)
    while T>0:
	    removal=sticksSorted[0]
	    count=0
	    for i in range(T):
	    	if sticksSorted[i]=removal:
	    		count+=1      
	  	del sticksSorted[:count]
	    T=len(sticksSorted)
	    print T

#The below is the right ANS

#!/usr/bin/py
def computeSticks(arr):
    arr.sort(reverse=True)
    while len(arr) > 0:
        print len(arr)
        block_cut = arr.pop()
        while len(arr) > 0 and arr[-1] == block_cut:
            arr.pop()
 
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    computeSticks(arr)