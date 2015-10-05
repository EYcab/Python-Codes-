__author__ = 'Chenxi'

# Enter your code here. Read input from STDIN. Print output to STDOUT
def findChildren(n):
    children = []
    for x in xrange(M):
        if edges[x][1] == n:
            children.append(edges[x][0])
            #nice recursion
            childN = findChildren(edges[x][0])
            for child in childN:
                children.append(child)
    return children
def generateTree():
    global tree
    for x in xrange(N):
        tree.append([x+1])
        print tree
    for x in xrange(N):
        d=tree[x].append(findChildren(x+1))
        print tree
    return tree
if __name__ == '__main__':
    N, M = map(int, raw_input().split())
    edges = []
    for x in xrange(M):
        u, v = map(int, raw_input().split())
        edges.append([u, v])

    info = []
    tree = []
    generateTree()
    count = 0

    for x in xrange(N):
        if len(tree[x][1]) % 2 == 1:
            count += 1
    #we have count-1 because we don't need the number of independent nodes but the number of nodes we cut
    #if we have n indep nodes, we need to cut n-1 edges to get the result
    print count - 1


