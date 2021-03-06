__author__ = 'Chenxi'
#a very nice use on the dictionary approach yet this approach has a run time shortage

from collections import Counter
import sys
if sys.version_info[0]>=3: raw_input=input
raw_input()
print(Counter(map(int,raw_input().split())).most_common()[-1][0])

#the {0] still works since that c.most_common()[-1] returns a tuple
# also attention here:
# Counter could directly eat in an array
#map(function, iterable, ...)
# Apply function to every item of iterable and return a list of the results.
# If additional iterable arguments are passed,
# function must take that many arguments
# and is applied to the items from all iterables in parallel.
# If one iterable is shorter than another it is assumed to be extended with None items.
# If function is None, the identity function is assumed; if there are multiple arguments,
#  map() returns a list consisting of tuples containing the corresponding items
# from all iterables (a kind of transpose operation).
#  The iterable arguments may be a sequence
# or any iterable object; the result is always a list.