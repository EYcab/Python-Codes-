if __name__=="__main__":
    N, M = map(int, raw_input().split())
    arr=[0]*(N+2)
    for _m in xrange(0, M):
        a,b,k = map(int, raw_input().split())
        arr[a]+=k
        arr[b+1]-=k
        print arr
    for n in xrange(2, N+1):
        arr[n]+=arr[n-1]
    print max(arr)
