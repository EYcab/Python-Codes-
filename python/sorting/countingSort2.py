# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()

ar = []
ar = map(int,raw_input().split())

times = [0]*100

for i in ar:
    times[i] += 1

for i in xrange(100):
    for c in xrange(times[i]):
        print i,
        
    
