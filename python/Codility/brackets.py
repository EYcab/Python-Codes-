# Short Problem Definition:
# Determine whether a given string of parentheses is properly nested.

# Link
# Brackets

# Complexity:
# expected worst-case time complexity is O(N);

# expected worst-case space complexity is O(N)

# Execution:
# Put every opening bracket on a stack. If a closing bracket is not the same as the top stack bracket, the string is not properly nested.


def isValidPair(left, right):
    if left == '(' and right == ')':
        return True
    if left == '[' and right == ']':
        return True 
    if left == '{' and right == '}':
        return True   
    return False
 
def solution(S):
    stack = []
     
    for symbol in S:
        if symbol == '[' or symbol == '{' or symbol == '(':
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return 0
            last = stack.pop()
            if not isValidPair(last, symbol):
                return 0
     
    if len(stack) != 0:
        return 0
             
    return 1