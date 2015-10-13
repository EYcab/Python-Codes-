__author__ = 'Chenxi'
# >>> from collections import Counter
# >>>
# >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# >>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>>
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>>
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]

# Also, in the below example, e[key] === value


import collections, sys
raw_input()
e = collections.Counter(map(int, sys.stdin.readline().strip('\r\n').split(" ")))
#print e
num = int(raw_input())
total = 0
for _ in xrange(num):
    key, price = map(int, sys.stdin.readline().strip('\r\n').split(" "))
    if e[key]:
        e[key]-=1
        total+=price
print total

