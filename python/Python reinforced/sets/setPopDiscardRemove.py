__author__ = 'Chenxi'
import sys
n = input()
s = set(map(int, raw_input().split()))
T = int(raw_input())
l = []
for i in xrange(T):
    e = list(map(str, sys.stdin.readline().strip('\n').split(" ")))
    l.append(e)
    #print l
for x in l:
    if x[0] == 'pop':
        s.pop()
    elif x[0]== 'remove':
        s.remove(int(x[1]))
    elif x[0]== 'discard':
        s.discard(int(x[1]))
print sum(s)

# education points
# Problem Statement
#
# .remove(x)
# This operation removes element x from set.
# If element x is not in the set, it raises a KeyError.
# .remove(x) operation returns None.
#
# Example
#
# >>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> s.remove(5)
# >>> print s
# set([1, 2, 3, 4, 6, 7, 8, 9])
# >>> print s.remove(4)
# None
# >>> print s
# set([1, 2, 3, 6, 7, 8, 9])
# >>> s.remove(0)
# KeyError: 0




# .discard(x)
# This operation also removes element x from set.
# But if element x is not in the set, it does not raises a KeyError.
# .discard(x) operation returns None.
#
# Example
#
# >>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> s.discard(5)
# >>> print s
# set([1, 2, 3, 4, 6, 7, 8, 9])
# >>> print s.discard(4)
# None
# >>> print s
# set([1, 2, 3, 6, 7, 8, 9])
# >>> s.discard(0)
# >>> print s
# set([1, 2, 3, 6, 7, 8, 9])



# .pop()
# This operation removes and return an arbitrary element from set.
# If there are no elements to remove, it raises a KeyError.
#
# Example
#
# >>> s = set([1])
# >>> print s.pop()
# 1
# >>> print s
# set([])
# >>> print s.pop()
# KeyError: pop from an empty set