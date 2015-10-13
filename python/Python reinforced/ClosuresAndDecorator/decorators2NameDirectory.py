__author__ = 'Chenxi'
#For sorting a nested list based on some parameter you can use itemgetter library.
#especially true if an array has multi-columns.key=itemgetter(2) the 2 is the position of the column

from operator import itemgetter

if __name__ == "__main__":
    n = int(raw_input())
    p = []
    for i in range(n):
        s = raw_input().split()
        p.append([s[0], s[1], int(s[2]), s[3]])
    sp = sorted(p, key=itemgetter(2))
    for i in sp:
        str = ''
        if i[3] == 'M':
            str += 'Mr. '
        else:
            str += 'Ms. '
        str += i[0] + ' ' + i[1]
        print str