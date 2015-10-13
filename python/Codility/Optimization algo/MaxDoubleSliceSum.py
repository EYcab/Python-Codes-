def solution(A):
    ending_here = [0] * len(A)
    starting_here = [0] * len(A)
     
    for idx in xrange(1, len(A)):
        ending_here[idx] = max(0, ending_here[idx-1] + A[idx])
     
    for idx in reversed(xrange(len(A)-1)):
        print idx
        starting_here[idx] = max(0, starting_here[idx+1] + A[idx])
        print idx, starting_here

    max_double_slice = 0
    print starting_here,ending_here
    for idx in xrange(1, len(A)-1):
        max_double_slice = max(max_double_slice, starting_here[idx+1] + ending_here[idx-1])
         
         
    return max_double_slice


 # In for idx in reversed(xrange(len(A)-1)): , 
 # reversed(xrange(len(A)-1)) means 
 # i.e. 5,4,3,2,1,0

#  Example test:    [3, 2, 6, -1, 4, 5, -1, 2] 
# Output:
# 6 here----------
# 6 [0, 0, 0, 0, 0, 0, 0, 0]
# 5 here----------
# 5 [0, 0, 0, 0, 0, 5, 0, 0]
# 4 here----------
# 4 [0, 0, 0, 0, 9, 5, 0, 0]
# 3 here----------
# 3 [0, 0, 0, 8, 9, 5, 0, 0]
# 2 here----------
# 2 [0, 0, 14, 8, 9, 5, 0, 0]
# 1 here----------
# 1 [0, 16, 14, 8, 9, 5, 0, 0]
# 0 here----------
# 0 [19, 16, 14, 8, 9, 5, 0, 0]
# [19, 16, 14, 8, 9, 5, 0, 0] [0, 2, 8, 7, 11, 16, 15, 17]
# OK 
