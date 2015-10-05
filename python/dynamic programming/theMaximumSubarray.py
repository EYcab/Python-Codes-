
def max_contiguous_subarray(L):
    current_sum = 0
    current_index = -1
    best_sum  = 0
    best_start_index = -1
    best_end_index = -1
    
    for i in range(len(L)):
        val = current_sum + int(L[i])
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
  # Iterate over the array. 
  #return L[best_start_index:best_end_index + 1]
    return best_sum
def max_noncontiguous_subarray(L):
    current_sum = 0
    for x in L:
        if x>0:
            current_sum+=x
    return current_sum
    
import sys

def check(result,L):
    if result==0:
        L.sort()
        return L[-1]
    else:
        return result
    

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        m = int(sys.stdin.readline())
        S = map(int,sys.stdin.readline().strip().split(' '))
        print check(max_contiguous_subarray(S),S), check(max_noncontiguous_subarray(S),S)