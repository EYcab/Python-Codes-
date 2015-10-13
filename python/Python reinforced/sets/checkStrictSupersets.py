__author__ = 'Chenxi'
s = set(raw_input().split())
result = False
for i in range(int(raw_input())): #More than 4 lines will result in 0 score. Do not leave a blank line also.
    A = set(raw_input().split())
    if s !=A.union(s) or s==A :
        print False
        exit()
else:
    print True


