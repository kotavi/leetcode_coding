"""
Given an array nums of integers, return how many of them contain an even number of digits.
....
Example 2:
    Input: nums = [555,901,482,1771]
    Output: 1
    Explanation:
        Only 1771 contains an even number of digits.

Constraints:
    1 <= nums.length <= 500
    1 <= nums[i] <= 10^5
"""
import unittest


def get_digits(num):
    res = []
    while num > 0:
        res.append(num % 10)
        num = num // 10
    return res


def find_numbers(nums):
    res = 0
    for num in nums:
        if len(get_digits(num)) % 2 == 0:
            res += 1
    return res


class Validation(unittest.TestCase):

    def test_empty_list(self):
        result = find_numbers([])
        self.assertEqual(find_numbers([]), 0,
                         "Expected: 0, Received: {}".format(result))

    def test_list_of_numbers(self):
        result = find_numbers([4, 133, 1, 177])
        self.assertEqual(result, 0,
                         "Expected: 1, Received: {}".format(result))

    def test_list_of_numbers_1(self):
        result = find_numbers([555, 901, 482, 1771])
        self.assertEqual(result, 1,
                         "Expected: 1, Received: {}".format(result))

    def test_list_of_numbers_2(self):
        result = find_numbers([8278, 6135, 3347, 2035, 4049, 6822, 724, 4394, 18, 7549, 4152, 7500, 7059, 2918,
                               354, 450, 2312, 7091, 8913, 7507])
        self.assertEqual(result, 17,
                         "Expected: 17, Received: {}".format(result))

    def test_list_of_numbers_3(self):
        result = find_numbers([2272, 4400, 3259, 9076, 418, 9668, 9469, 8021, 9773, 9690, 3046, 6700, 2808, 7542, 2647,
                               2060, 7631, 7292, 2823, 6201, 4986, 5790, 9329, 5707, 8479, 4998, 4016, 4299, 6686,
                               2517, 4451, 5264, 3445, 6437, 1264, 6419, 3729, 7116, 4054, 5942, 4082, 2643, 9782,
                               5385, 5188, 2189, 3699, 7762, 8520, 6084, 8714, 4761, 3888, 9831, 7572, 1178, 5777,
                               773, 6306, 9034, 7923, 5188, 2543, 3044, 1220, 205, 2130, 9287, 2691, 3332, 9312, 8165,
                               7921, 9868, 8290, 2204, 2713, 9644, 956, 98, 1865, 1433, 3676, 7480, 484, 5626, 9548,
                               5868, 7428, 7971, 5870, 9242, 732, 685, 6424, 7772, 5778, 6501, 8301, 6900, 3815, 9933,
                               3572, 5142, 9567, 5981, 7169, 3658, 1175, 28, 3231, 9813, 9133, 5086, 5673, 8497, 7808,
                               453, 6492, 6160, 9555, 3721, 788, 1870, 3097, 6681, 2273, 9331, 9625, 5302, 7076, 3706,
                               6193, 743, 4345, 8941, 5287, 6442, 1162, 6502, 3735, 8489, 4489, 5797, 4609, 1259, 5127,
                               2454, 4252, 448, 1157, 730, 3071, 768, 750, 5867, 1109, 4095, 2609, 7057, 1301, 465,
                               7704, 2770, 5417, 9980, 6447, 4854, 8913, 349, 4364, 7448, 1398, 2342, 427, 704, 2198,
                               329, 6353, 961, 4158, 3269, 500, 461, 671, 4145, 2492, 4924, 4472, 1390, 17, 6090, 1199,
                               1754, 6722, 2123, 8828, 4950, 8914, 4692])
        self.assertEqual(result, 177,
                         "Expected: 17, Received: {}".format(result))