#!/usr/bin/env python
#there are 3 sets of codes here
#Funny string in strings


import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        S = list(map(ord, sys.stdin.readline().strip()))
        
        diff = [abs(x - S[i - 1]) for i, x in enumerate(S) if i > 0]
        print('Funny' if diff == diff[::-1] else 'Not Funny')

#the above S[i]==x
-----------------------------------------------------------------
# equivalent to the below:

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        S = list(map(ord, sys.stdin.readline().strip()))
        
        diff = [abs(S[i] - S[i - 1]) for i in range(len(S)) if i > 0]
        print('Funny' if diff == diff[::-1] else 'Not Funny')


	for i in range(len(L)):
		val = current_sum + L[i]
        if val > 0:
            if current_sum == 0:
              current_index = i
            current_sum = val
        else:
          current_sum = 0

        if current_sum > best_sum:
          best_sum = current_sum
          best_start_index = current_index
          best_end_index = i
        





n = input()
numbers = [i for i in input().split()]
if __name__ == '__main__':
    for inNum in sort(numbers):
        if number == int(inNum):
            count += 1
    print (count ,end =" ",flush=True)