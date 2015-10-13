__author__ = 'Chenxi'
import sys
if sys.version_info[0]>=3:
    raw_input=input
raw_input()
X=[int(e) for e in raw_input().split()]
A={int(e) for e in raw_input().split()}
B={int(e) for e in raw_input().split()}
total=0
for e in X:
	total+=(e in A)-(e in B)
print(total)

#Set application  and boolean results

#The question is in No Idea at Python in Hackerrank