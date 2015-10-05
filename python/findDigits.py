import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
    	N = int(sys.stdin.readline())
        digits = list(map(int, str(N)))
        print(sum(digits.count(i) for i in range(1, 10) if i in digits and N%i ==0))

