__author__ = 'Chenxi'
#!/usr/bin/py

if __name__ == '__main__':
    n = input()
    k = input()
    candies = [input() for _ in range(0,n)]
    candies.sort()
    min_diff = 1000000000
    ## Write code here to compute the answer using (n, k, candies)

    #the nature of this question is to 
    #calculate the minimum gap of each clustered group after the sorted
 
    for i in xrange(n - k + 1):
        min_diff = min(min_diff, candies[i+k-1] - candies[i])
     
    print min_diff
    #the above candies[i] is the best min element to go after since 
    #the clustered tested may be way longer than our expected k in length