def red(c):
    i = c/5
    c = c%5
    i+= c/2
    c = c%2
    i+= c
    return i
for _ in xrange(input()):
    input()
    C = map(int,raw_input().split())
    if C:
        m = min(C)
        print min(sum(red(c-m+i) for c in C) for i in xrange(5))
    else:
        print 0