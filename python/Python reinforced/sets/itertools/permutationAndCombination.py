__author__ = 'Chenxi'
#permutation:

#!/usr/bin/python
import sys,itertools
if sys.version_info[0]>=3: raw_input=input
a,b=raw_input().split()
for e in itertools.permutations(sorted(a),int(b)):
    print(''.join(e))

#Observably, itertools.permutations(sorted(a),int(b)) is solving everything.
#a has to be sorted to get a sorted result directly
#


# examples
# >>> from itertools import permutations
# >>> print permutations(['1','2','3'])
# <itertools.permutations object at 0x02A45210>
# >>>
# >>> print list(permutations(['1','2','3']))
# [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
# >>>
# >>> print list(permutations(['1','2','3'],2))
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
# >>>
# >>> print list(permutations('abc',3))
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]


#Combination:
import sys,itertools
if sys.version_info[0]>=3: raw_input=input
a,b=raw_input().split()
n = int(b)+1
for i in range(1,n):
    for e in itertools.combinations(sorted(a), i ):
        print(''.join(e))


#Combination with replacement
import sys,itertools
if sys.version_info[0]>=3: raw_input=input
a,b=raw_input().split()
for e in itertools.combinations_with_replacement(sorted(a),int(b)):
    print(''.join(e))
#
# >>> from itertools import combinations_with_replacement
# >>>
# >>> print list(combinations_with_replacement('12345',2))
# [('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
# >>>
# >>> A = [1,1,3,3,3]
# >>> print list(combinations(A,2))
# [(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]

# result:
# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK



