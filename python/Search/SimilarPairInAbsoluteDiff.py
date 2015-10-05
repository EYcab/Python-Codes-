__author__ = 'Chenxi'
# Enter your code here. Read input from STDIN. Print output to STDOUT
from bisect import insort, bisect_left, bisect_right
import sys

def search(parent, children, root, T, N):
    # node is for checking index and its existence purpose
    # stack is to find index of values array to delete an element whenever len(values) is bigger than 2
    # value is for the binary index search purpose
    node = root
    total = 0
    stack = [node]
    values = [node]
    while node:
        print "node_start",node
        if children[node]:
            c = node = children[node].pop()
            #print node
            m, x = c - T, c + T
            #print "m,x",m, x

            #a binary way to count the possible pairs
            im = bisect_left(values, m)
            ix = bisect_right(values, x)
            #print im, ix, values
            total += ix - i
            insort(values, c)
            #print "values:",values
            stack.append(c)
        else:
            print "stack:",stack
            values.pop(bisect_left(values, stack.pop()))
            node = parent[node]
            print "node:",node
    print stack,values
    return total
#children = [[], [], [], [], [], []]
#because our distance is set to have plus and minus,thus the smallest number has to less 1
#whereas the largest number has to be plus 1, both of them creates 2 new elements
#also as n points yields n-1 edges, thus the children elements expended to n+1
fin = sys.stdin
if __name__=='__main__':
    n, T = map(int, fin.readline().split())
    children = [[] for i in xrange(n + 1)]
    print children
    parent = [None] * (n + 1)
    root = 0
    for i in range(n-1):
        si, ei = map(int, fin.readline().split())
        children[si].append(ei)
        #print children,"-------------------"
        parent[ei] = si
        #print parent[ei]
        if root == 0 or ei == root:
            root = si
    #eventually children == [[], [4,5], [], [2,1], [], []]
    #parent ==[None, 3, 3, None, 1, 1]
    #root ==3
    #print parent
    #print "root:", root
    print search(parent, children, root, T, n)