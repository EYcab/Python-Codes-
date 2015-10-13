__author__ = 'Chenxi'

# The given mobile numbers may have +91 or 91 or 0 written before the actual 10 digit number. Alternatively, there maynot be any prefix at all.
#
# Input Format
#
# An integer N followed by N mobile numbers.
#
# Output Format
#
# N mobile numbers printed in different lines in the required format.
#
# Sample Input
#
# 3
# 07895462130
# 919875641230
# 9195969878
# Sample Output
#
# +91 78954 62130
# +91 91959 69878
# +91 98756 41230

number = []

N = int(raw_input())
for i in range(N):
    number.append(str(raw_input()))

def mobile(function):
    def input(number):
            return sorted([function(i) for i in number])
    return input

@mobile
def standardize(number):
    return "+91" + " " + number[-10:-5] + " " + number[-5:]

print '\n'.join(standardize(number))

#the "+91" + " " + number[-10:-5] + " " + number[-5:]
# is a re-adding elements method