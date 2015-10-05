def next(a):
    i = len(a) - 2
    while not (i < 0 or a[i] < a[i+1]):
        i -= 1
    if i < 0:
        return False
    j = len(a) - 1
    while not (a[j] > a[i]):
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i+1:] = reversed(a[i+1:])
    return True
for i in xrange(input()):
    w = list(raw_input().strip())
    if next(w):
        print ''.join(w)
    else:print 'no answer'
    