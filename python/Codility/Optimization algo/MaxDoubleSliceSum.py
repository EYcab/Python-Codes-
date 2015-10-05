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
