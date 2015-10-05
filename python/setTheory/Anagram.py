#Both ways work
#Yet the 1st one works faster
import collections, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        s = sys.stdin.readline().strip()
        
        if len(s) % 2:
            print(-1)
        else:
            s1, s2 = s[: len(s) // 2], s[len(s) // 2 :]
            c1 = collections.Counter(s1)
            c2 = collections.Counter(s2)

     		length = sum(min(c1[c], c2[c]) for c in (set(s1) & set(s2)))
     		print((len(s1) - length) + (len(s2) - length))/2


# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections, sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        s = sys.stdin.readline().strip()
        
        if len(s) % 2:
            print(-1)
        else:
            s1, s2 = s[: len(s) // 2], s[len(s) // 2 :]
            c1 = collections.Counter(s1)
            c2 = collections.Counter(s2)
            replacements = len(s1)
            
            for c in s1:
                if c in c2 and c2[c] > 0:
                    replacements -= 1
                    c2[c] -= 1
            
            print(replacements)
            