__author__ = 'Chenxi'
import sys

if __name__ == '__main__':
    testCases = int(sys.stdin.readline())
    for t in xrange(testCases):
        num = int(sys.stdin.readline())
        grid = []
        gridRowSorted = []
        judge = True
        for x in (list(sys.stdin.readline().strip('\n')) for m in xrange(num)):
            x.sort()
            grid.append(x)
        print grid
        for i in range(1,num):
            for j in range(num):
                if grid[i-1][j] >grid[i][j]:
                    judge = False
        print judge
