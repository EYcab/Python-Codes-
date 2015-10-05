__author__ = 'Chenxi'
#!/usr/bin/env python

import sys, copy
def check(oldArr, arrInOrder):
    if arrInOrder == arr:
        print " ".join(map(str, arr))
        exit()
if __name__ == '__main__':
    num, SwapMax = list(map(int, sys.stdin.readline().split()))
    arr = map(int, sys.stdin.readline().split())
    arrInOrder=sorted(arr)
    #print arr, arrInOrder
    arrInOrder.reverse()
    rightArr = copy.copy(arrInOrder)
    #print rightArr
    check(arr,rightArr)

    arrInOrder.reverse()
    #print arrInOrder
    i, x = 0, 0
    x = arrInOrder.pop()
    while SwapMax>0:
        if arr[i]!=x:
            arr[arr.index(x)] =arr[i]
            arr[i]=x
            SwapMax-=1
        i+=1
        check(arr, rightArr)

    print " ".join(map(str, arr))

