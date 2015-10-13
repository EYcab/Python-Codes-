__author__ = 'Chenxi'
import sys

import sys
if sys.version_info[0]>=3: raw_input=input
raw_input()
s1=set(map(int,raw_input().split()))
raw_input()
s2=set(map(int,raw_input().split()))
print(len(s1.union(s2)))

#Union
import sys
if sys.version_info[0]>=3: raw_input=input
raw_input()
s1=set(map(int,raw_input().split()))
raw_input()
s2=set(map(int,raw_input().split()))
print(len(s1.intersection(s2)))
# s1 -s2
print(len(s1.difference(s2)))

print(len(s1.symmetric_difference(s2)))
#here, intersection is more strict than union in operation

# >>> s = set("Hacker")
# >>> print s.intersection("Rank")
# set(['a', 'k'])
#
# >>> print s.intersection(set(['R', 'a', 'n', 'k']))
# set(['a', 'k'])
#
# >>> print s.intersection(['R', 'a', 'n', 'k'])
# set(['a', 'k'])
#
# >>> print s.intersection(enumerate(['R', 'a', 'n', 'k']))
# set([])
#
# >>> print s.intersection({"Rank":1})
# set([])
#
# >>> s & set("Rank")
# set(['a', 'k'])