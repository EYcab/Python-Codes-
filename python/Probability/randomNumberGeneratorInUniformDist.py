import fractions

def D():
    A,B,C = input().split(' ')
    A = int(A)
    B = int(B)
    C = int(C)
    if ( A > B ):
        A,B = B,A
    ans = 0
    S = A*B*2
    if ( C < A ):
        ans = fractions.Fraction(C*C,S)
    elif ( C < B ):
        ans = fractions.Fraction(2*A*C-A*A,S)
    elif ( C >= A+B ):
        ans = 1
    else:
        ans = fractions.Fraction(C*C-(C-A)**2-(C-B)**2,S)
    if ( ans >= 1 ):
        print('1/1')
    else:
        print(ans)

t = int(input())
while ( t > 0 ):
    t -= 1
    D()