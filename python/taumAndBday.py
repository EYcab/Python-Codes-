import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        NumB, NumW = list(map(int, sys.stdin.readline().split()))
        priceB,priceW,priceT = list(map(int, sys.stdin.readline().split()))
        
        if priceB > priceW + priceT:
        	total = priceW*(NumW+NumB) + priceT*NumB
        elif priceW > priceB + priceT:
        	total = priceB*(NumB+NumW) + priceT*NumW
       	else:
       		total = priceB*NumB + priceW*NumW
       	print total
