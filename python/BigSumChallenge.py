# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    print(sum(map(int, sys.stdin.readline().split())))