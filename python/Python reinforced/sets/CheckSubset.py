__author__ = 'Chenxi'
for i in range(int(raw_input())): #More than 4 lines will result in 0 score. Do not leave a blank line also.
    a = int(raw_input()); A = set(raw_input().split())
    b = int(raw_input()); B = set(raw_input().split())
    print(B ==A.union(B))