__author__ = 'Chenxi'
import bisect
#bisect.bisect_right(done, x) is to find the element "x" 's inserted position starting from 0
#and bisect_right even take account of x position i.e.
#h= bisect.bisect_right([1,2,3,4,5,6,7,8,9], 8)
#print h --- "8"
#m= bisect.bisect_left([1,2,3,4,5,6,7,8,9], 8)
#print h --- "7"
def max_mod(array, M):
    L = [0] * (len(array) + 1)
    print L
    for i in range(1, len(L)):
        L[i] = L[i - 1] + array[i - 1]
    print L
    #acc is to store the result
    acc = 0
    #done array stores the modulo list
    done = []
    # print L
    for i in range(len(L)):
        x = L[i] % M
        j = bisect.bisect_right(done, x)
        #print x, j, "---------------------------------"
        acc = max(acc, x)
        # print done, (x, j), acc

        # if there is new injected modulo's position
        #  acc = max(acc, (L[i] - done[j]) % M)
        # tries to find the possible new module result
        # which is from the sum of the meddle of the number sequence
        if j < i:
            acc = max(acc, (L[i] - done[j]) % M)
        done.insert(j, x)
    return acc

for _ in range(input()):
    N, M = map(int, raw_input().split(" "))
    array = map(int, raw_input().split(" "))
    print max_mod(array, M)