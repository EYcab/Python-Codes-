#!/bin/python

# Head ends here
def partition(n,ar):
    p=ar[0]
    lt=[]
    rt=[]
    for i in range(1,n):
        if(ar[i]<=p):
            lt.append(ar[i])
        else:
            rt.append(ar[i])
    print " ".join(map(str,lt)) + " " + str(p) + " " +" ".join(map(str,rt))
    return ""

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(m,ar)