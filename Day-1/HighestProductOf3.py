import unittest, math


def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers
    
    assert(len(list_of_ints) >= 3)
    maxA = -float("inf")
    maxB = -float("inf")
    maxC = -float("inf")
    minA = float("inf")
    minB = float("inf")
    
    for e in list_of_ints:
        if e > maxA:
            maxC = maxB
            maxB = maxA
            maxA = e
        
        elif e > maxB:
            maxC = maxB
            maxB = e
        
        elif e > maxC:
            maxC = e
            
        if e < minA:
            minB = minA
            minA = e
            
        elif e < minB:
            # print(e)
            minB = e
    return max(minA * minB * maxA, maxA * maxB * maxC)


















# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)
