# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/py
 
def sherlockBeast(N):     
    three_cnt = N/3
    five_cnt = 0
     
    while three_cnt >=0:
        rem = N - three_cnt*3
        if rem % 5 == 0:
            five_cnt = rem/5
            break
        three_cnt -= 1
         
    if three_cnt <= 0 and five_cnt == 0:
        return "-1"
     
    return "555"*three_cnt + "33333"*five_cnt
 
if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        n = input()
        print sherlockBeast(n)