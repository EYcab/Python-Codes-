__author__ = 'Chenxi'
#A very interesting operation
# getattr(object, name[, default])¶
# Return the value of the named attribute of object. name must be a string.
# If the string is the name of one of the object’s attributes,
# the result is the value of that attribute.
#  For example, getattr(x, 'foobar') is equivalent to x.foobar.

# If the named attribute does not exist,
# default is returned if provided, otherwise AttributeError is raised.

import sys
if sys.version_info[0]>=3: raw_input=input
raw_input()
s=set(map(int,raw_input().split()))
for _ in range(int(raw_input())):
	a=raw_input().split()
	getattr(s,a[0])(set(map(int,raw_input().split())))
print(sum(s))


