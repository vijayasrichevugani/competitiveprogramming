def ParanthesisCount(n):
    result = []
    generateParenthesis(result, "", n, n)
    return result
def generateParenthesis(result, current, left, right):
    if left == 0 and right == 0:
        result.append(current)
    if left > 0:
        generateParenthesis(result, current + "(", left - 1, right)
    if left < right:
        generateParenthesis(result, current + ")", left, right - 1)

print (ParanthesisCount(2)), len(ParanthesisCount(2))
print (ParanthesisCount(3), len(ParanthesisCount(3)))
print (ParanthesisCount(5), len(ParanthesisCount(5)))
print (ParanthesisCount(4), len(ParanthesisCount(4)))
print (ParanthesisCount(1), len(ParanthesisCount(1)))
print (ParanthesisCount(6), len(ParanthesisCount(6)))
