# Enter your code here. Read input from STDIN. Print output to STDOUT
def getDiagonalDiff(v):
    diff = 0
    v_len = len(v)
    s1 =0
    s2 =0
    for idx in range(0,v_len):
        s1 += v[idx][idx]
        s2 += v[idx][v_len- 1 -idx ]
    return abs(s1-s2)

if __name__ == '__main__':
    n = input() 
    myVal = []
    for _ in xrange(n):
        e = map(int, raw_input().split())
        myVal.append(e)
print getDiagonalDiff(myVal)



