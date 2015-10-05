import collections, sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = collections.Counter(map(int, sys.stdin.readline().split()))
    
    n = N
#below k means collection key in memory  
#A[K] means the value of the key after A is sorted 
#this structure is like pooling dictionary layers one by one
    for k in sorted(A):
        print(n)
        n -= A[k]

