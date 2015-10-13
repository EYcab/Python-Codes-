# A very interesting case to learn defaultdict by collections
# here,also print(' '.join(map(str,d[s]))) is very important to notice

from collections import defaultdict
import sys

if sys.version_info[0]>=3: 
	raw_input=input

N,M=map(int,raw_input().split())
d=defaultdict(list)
for i in range(N):
	s=raw_input().rstrip()
	d[s].append(i+1)
for _ in range(M):
	s=raw_input().rstrip()
	#s in d because we need to check if s in d 
	#here we use element check approach
	if s in d:
		print(' '.join(map(str,d[s])))
	else:
		print('-1')





# You could convert it to a string instead of printing the list directly:

# print(", ".join(LIST))
# If the elements in the list aren't strings, you can convert them to 
#string using either repr (if you want quotes around strings) 
#or str (if you don't), like so:

# LIST = [1, "foo", 3.5, { "hello": "bye" }]
# print( ", ".join( repr(e) for e in LIST ) )
# Which gives the output:

# 1, 'foo', 3.5, {'hello': 'bye'}