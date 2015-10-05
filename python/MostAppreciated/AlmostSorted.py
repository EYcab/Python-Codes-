N = input()
arr = map(int, raw_input().split())
sarr = sorted(arr)
bad_range = []
for i in range(len(arr)):
    if arr[i] != sarr[i]:
        bad_range.append(i)
if len(bad_range) == 2:
    print 'yes'
    print 'swap', bad_range[0]+1, bad_range[-1]+1
else:
    bad = False
    for i in range(len(bad_range)-1):
        if arr[bad_range[i]] < arr[bad_range[i+1]]:
            print 'no'
            bad = True
            break
    if not bad:
        print 'yes'
        print 'reverse', bad_range[0]+1, bad_range[-1]+1