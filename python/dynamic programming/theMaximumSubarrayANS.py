# Enter your code here. Read input from STDIN. Print output to STDOUT
class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        N, A = cipher
        # SPECIAL CASE
        maxa = max(A)
        if maxa<0:
            return "%d %d"%(maxa, maxa)
        sum_b = sum(filter(lambda x: x>0, A))

        sum_a = 0
        current_sum = 0
        for a in A:
            current_sum += a
            if current_sum<0:
                current_sum = 0
            sum_a = max(sum_a, current_sum)

        return "%d %d"%(sum_a, sum_b)
import sys

if __name__=="__main__":
    #f = open("1.in", "r")
    f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        N = int(f.readline().strip())
        A = map(int, f.readline().strip().split(' '))
        cipher = N, A
        # solve
        s = "%s"%(solution.solve(cipher))
        print s