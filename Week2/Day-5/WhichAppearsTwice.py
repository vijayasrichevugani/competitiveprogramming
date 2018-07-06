def find_repeat(numbers_list):

    # Find the number that appears twice
    x = len(numbers_list)-1
    p = x*(x+1)/2
    q = 0
    for i in numbers_list:
        q += i

    return q - p

# Tests

actual = find_repeat([1, 2, 1])
expected = 1
print(actual == expected)

actual = find_repeat([4, 1, 3, 4, 2])
expected = 4
print(actual == expected)

actual = find_repeat([1, 5, 9, 7, 2, 6, 3, 8, 2, 4])
expected = 2
print(actual == expected)
