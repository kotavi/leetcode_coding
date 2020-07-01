"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
    Input: [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s.
        The maximum number of consecutive 1s is 3.
Note:
    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000
"""
import unittest


def max_number_of_consecutive_ones(arr):
    count = 0
    max_number = 0
    for num in arr:
        if num == 1:
            count += 1
            max_number = max(max_number, count)
        else:
            count = 0
    return max_number


class Validation(unittest.TestCase):

    def test_empty_list(self):
        response = max_number_of_consecutive_ones([])
        self.assertTrue(response == 0,
                        'Expected: 0, received: {}'.format(response))

    def test_list_with_one_element(self):
        response = max_number_of_consecutive_ones([1])
        self.assertTrue(response == 1,
                        'Expected: 1, received: {}'.format(response))

    def test_list_with_one_element_2(self):
        response = max_number_of_consecutive_ones([0])
        self.assertTrue(response == 0,
                        'Expected: 0, received: {}'.format(response))

    def test_list_with_ones_and_zeros(self):
        response = max_number_of_consecutive_ones([1, 1, 0, 1, 1, 1])
        self.assertTrue(response == 3,
                        'Expected: 3, received: {}'.format(response))

    def test_list_with_ones_and_zeros_2(self):
        response = max_number_of_consecutive_ones([1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1])
        self.assertTrue(response == 4,
                        'Expected: 4, received: {}'.format(response))

    def test_list_with_ones_and_zeros_3(self):
        response = max_number_of_consecutive_ones([1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1,
                                                   0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
                                                   0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1,
                                                   1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1,
                                                   0, 0, 1, 1, 0, 1, 1, 1])
        self.assertTrue(response == 8,
                        'Expected: 8, received: {}'.format(response))

