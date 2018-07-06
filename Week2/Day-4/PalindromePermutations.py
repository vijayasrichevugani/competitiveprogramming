def has_palindrome_permutation(str):

    # Check if any permutation of the input is a palindrome
    dic = {}
    for i in str:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    
    flag = 0
    for i in dic:
        if dic[i]%2==1:
            flag+=1

    return flag==1 or flag==0

# Tests

result = has_palindrome_permutation('aabcbcd')
expected = True
print(result == expected)

result = has_palindrome_permutation('aabccbdd')
expected = True
print(result == expected)

result = has_palindrome_permutation('aabcd')
expected = False
print(result == expected)

result = has_palindrome_permutation('aabbcd')
expected = False
print(result == expected)

result = has_palindrome_permutation('')
expected = True
print(result == expected)

result = has_palindrome_permutation('a')
expected = True
print(result == expected)
