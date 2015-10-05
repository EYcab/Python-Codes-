#!/bin/python

# Head ends here
def partition(ar):    
  if len(ar) <= 1:
    return ar


  p = ar[0]
  lower = [x for x in ar[1:] if x <= p]
  higher = [x for x in ar[1:] if x > p]
  result = partition(lower) + [p] + partition(higher)
  print ' '.join(str(n) for n in result)
  return result

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)