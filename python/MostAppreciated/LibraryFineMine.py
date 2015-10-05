import sys


if __name__ == '__main__':
    #state of the act list(map())
    D_actual, M_actual, Y_actual = list(map(int, sys.stdin.readline().split()))
    D_expected, M_expected, Y_expected = list(map(int, sys.stdin.readline().split()))

    if Y_actual > Y_expected:
        print(10000)
    elif M_actual > M_expected and Y_actual == Y_expected:
        print(500 * (M_actual - M_expected))
    elif D_actual > D_expected and M_actual == M_expected:
        print(15*(D_actual-D_expected))
    else: 
        print 0