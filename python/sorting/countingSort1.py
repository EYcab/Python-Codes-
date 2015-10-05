import sys

l = [0] * 100
data = sys.stdin.readlines()
vals = map(int, data[1].strip().split(' '))

for val in vals:
    l[val] += 1
    #print l

print ' '.join(map(str, l))