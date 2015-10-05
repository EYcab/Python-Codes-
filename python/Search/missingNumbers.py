__author__ = 'Chenxi'
# Python 3 code: missing Number in Search
#the basic method is to store all the strings and count them in dictionary format
#then identify existent string in the form and clean up the dictionary record
#sort and print the output
import sys
def findMissingNumber(sample,form):
    A = {}
    for s in sample:
        if s not in A:
            A[s] = 0
        A[s] += 1
    #print (A)  ----------------- {208: 1, 203: 2, 204: 2, 205: 2, 206: 2, 207: 1}
    for f in form :
        A[f] -= 1

    print(*sorted(k for k in A if A[k]))

if __name__ == '__main__':
    numSample = int(sys.stdin.readline())
    sample = map(int, sys.stdin.readline().split())
    numForm = int(sys.stdin.readline())
    form = map(int, sys.stdin.readline().split())

    findMissingNumber(sample,form)

