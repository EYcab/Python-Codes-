__author__ = 'Chenxi'
import sys
if sys.version_info[0]>=3: raw_input=input
N = int(raw_input())
A = [0,1]
if __name__ == "__main__":
    for i in range(2,N):
        A.append(A[i-1]+A[i-2])
    print map(lambda a: a*a*a,A)[:N]

#Note:
# lambda iteration is like a for loop starting from A[0]
#if N = 1, we need to have only 1 element,
# so [:N] helps saving only the 1st N elements is in the output
