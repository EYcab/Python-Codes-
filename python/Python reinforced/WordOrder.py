__author__ = 'Chenxi'
#!/usr/bin/python
import sys
if sys.version_info[0]>=3: raw_input=input
#   h = {} is another good way to declare a dictionary h is set
h={}
for i in range(int(raw_input())):
	s=raw_input().rstrip()
	if s not in h:
		h[s]=[i,0]
	h[s][1]+=1
print(len(h))
#print h.items()

# result: [('bcde', [2, 1]), ('abcdefg', [1, 1]), ('bcdef', [0, 2])]

# below the h.value() pointing directly to the 1st item inside [d,j]


print(' '.join(str(e[1]) for e in sorted(h.values())))

#explanation to the dictionary codes
# the above s is the key of the item and is separated from its value by ":"
# thus the above [i,0] is each item's value.
# h[s][1]+=1  means {...."s":[i, j+1],....}
#h.items() shows its items