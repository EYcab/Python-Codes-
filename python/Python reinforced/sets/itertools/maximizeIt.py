__author__ = 'Chenxi'
#This project is from maximize it in Python at hackerrank
import sys,itertools
if sys.version_info[0]>=3: raw_input=input
lines,M=map(int,raw_input().split())
a=[[int(e)**2 for e in raw_input().split()][1:] for _ in range(lines)]
print(max(sum(e)%M for e in itertools.product(*a)))

# IN  a=[[int(e)**2 for e in raw_input().split()][1:] for _ in range(lines)]
# the [1:] is to delete the label part of the iteration calculation result

#A very nice SQL like list-comprehension note by [int(e)**2 for e in raw_input().split()][1:]