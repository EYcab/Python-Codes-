__author__ = 'Chenxi'

from collections import deque
#the dist is a array mode of -1 and so it would be change later for recording
#deque is a deque([]) like passenger for delivering
#the Q.popleft() clearing all the popped out element starting from the left
#D is a set yet it is just like array D[0] means the first set's element collections
#which has 1 and 2
def bfs(D, Origin):
    dist = [-1] * len(D)
    Q = deque()
    #print Q
    Q.append((Origin, 0))
    #print Q ----deque([(0, 0)])
#Use v,d from the Deque to iterate through the dist array of -1 to
    while Q:
        #print dist,"------------------------"
        v, d = Q.popleft()
        # print v, d
        # print Q
        # if dist element is changed then restart the whole loop process
        if dist[v] > -1:
            continue
        #as long as dist[v] is unchanged, then dist[v] is assigned to a new value immediately
        dist[v] = d
        #print D[v], v, "!!!!!!!!!!!!!!!!! Print the D"
        for n in D[v]:
            #D[v] means the elements inside set([x,y]),which are x and y
            #print n, dist[n]
            if dist[n] == -1:
                Q.append((n, d+6))
    #in the sample,after 1st round Q has deque([1,6],[2,6])
    #pop the origin position's value
    #in the final round it replaces the first 0 with 6 and next pop the last elements

    #.pop() is set to auto-eliminate the rightest element yet if we have .pop(var)
    #the appointed var is cleared instead
    dist.pop(Origin)
    return dist

T = input()
for _ in xrange(T):
    N, M = map(int, raw_input().split())
    # construct Sets like {0: set([1, 2]), 1: set([0]), 2: set([0]), 3: set([])}
    D = {i: set() for i in xrange(N)}
    for _ in xrange(M):
        x, y = map(int, raw_input().split())
        D[x-1].add(y-1)
        D[y-1].add(x-1)
    origin = input() - 1
    print D
    L = map(str, bfs(D, origin))
    print " ".join(L)