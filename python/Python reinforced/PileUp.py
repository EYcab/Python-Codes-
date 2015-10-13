__author__ = 'Chenxi'
import sys
if sys.version_info[0]>=3: raw_input=input
T = int(raw_input())
for _ in xrange(T):
	raw_input()
	a=[(int(e),i) for i,e in enumerate(raw_input().split())]
	#print a
	mi_idx=min(a)[1]
	#print "mi: ", mi_idx
	#print a[:mi_idx] , a[mi_idx:]
	print('Yes' if all(sorted(e)==e for e in ([e[0] for e in reversed(a[:mi_idx])],a[mi_idx:])) else 'No')

#because we wanna get a black hole structure for a 1 dimension value line
#where the middle has the smallest value
#thus,as long as we reverse the 1st half and observe if the 1st half is as sorted as the 2nd half
#Here, again, an reversed() sort is not a value reversed sort but a key-reversed sort,
# Thus the value was not disordered

#
# [(4, 0), (3, 1), (2, 2), (1, 3), (3, 4), (4, 5)]
# mi:  3
# [(4, 0), (3, 1), (2, 2)] [(1, 3), (3, 4), (4, 5)]
# Yes
# [(1, 0), (3, 1), (2, 2)]
# mi:  0
# [] [(1, 0), (3, 1), (2, 2)]
# No


# -------------------------------------------------------------------------------------------
# import sys
# if sys.version_info[0]>=3: raw_input=input
# T = int(raw_input())
# for _ in range(T):
# 	raw_input()
# 	a=[(int(e),i) for i,e in enumerate(raw_input().split())]
# 	print a
# 	mi_idx=min(a)[1]
# 	#print "mi: ", mi_idx
# 	#print a[:mi_idx] , a[mi_idx:]
# 	for e in reverse(a[:mi_idx]):
# 		print e[0]
# 	for e in ([e[0] for e in reversed(a[:mi_idx])],a[mi_idx:]):
# 		print e
# [2, 3, 4] [(1, 3), (3, 4), (4, 5)]
# 	#print('Yes' if all(sorted(e)==e for e in ([e[0] for e in reversed(a[:mi_idx])],a[mi_idx:])) else 'No')

