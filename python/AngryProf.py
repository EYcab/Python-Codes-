import sys
def quicksort(lst):
        if len(lst) == 0:
            return []
        else:
            return quicksort([x for x in lst[1:] if x < lst[0]]) + [lst[0]] + \
                   quicksort([x for x in lst[1:] if x >= lst[0]])
def checkCancel():
    pop_total, pop_bound = list(map(int, sys.stdin.readline().split()))    
    e = list(map(int, sys.stdin.readline().split()))
    ls = quicksort(e)
    num = 0
    for x in ls:
        if x <=0:
            num+=1
    if(pop_bound>num):
        print "YES"
    else:
        print "NO"
        
if __name__ == '__main__':
    n = int(raw_input())
    for i in xrange(n):
        checkCancel()

    
    
    