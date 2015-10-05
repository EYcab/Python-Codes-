T = int(input())
for _ in range(0, T):
    n, k = map(int, input().strip().split())
    arr = [int(i) for i in input().strip().split()]

    dp = [0] * (k + 1)
    arr.sort()
    for g in range(1, k + 1):     # k slots in knapsack
        for i in range(0, n):    # for each candidate
            if arr[i] <= g:                
                dp[g] = max(dp[g], arr[i] + dp[g - arr[i]])
    print (dp[k])

#Attention to the above: the dp is decleared as a list in k+1 len