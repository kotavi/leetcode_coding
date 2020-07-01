"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:
    Input:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3
    Output: [1,2,2,3,5,6]

Constraints:
    -10^9 <= nums1[i], nums2[i] <= 10^9
    nums1.length == m + n
    nums2.length == n
"""


def merge(nums1, m, nums2, n):
    """
    Approach: use 3 pointers
    1) index - to traverse nums1 starting from the end
    2) nums1_ind - to traverse actual elements of nums1
    3) nums2_ind - to traverse actual elements of nums2

    Time Complexity: O(N), where N is the length of nums1.
    Space Complexity: O(1).
    """
    index = len(nums1) - 1
    nums1_ind = m - 1
    nums2_ind = n - 1
    while index >= 0 and nums2_ind >= 0:
        if nums1[nums1_ind] > nums2[nums2_ind] and nums1_ind >= 0:
            nums1[index] = nums1[nums1_ind]
            nums1_ind -= 1
        else:
            nums1[index] = nums2[nums2_ind]
            nums2_ind -= 1
        index -= 1
    return nums1


print(merge([0, 0, 0, 0], 0, [2, 4, 5, 6], 4))
print(merge([1, 2, 3, 0, 0, 0, 0], 3, [2, 4, 5, 6], 4))
print(merge([1, 2, 3, 5, 0, 0, 0, 0, 0], 4, [-1, 2, 4, 5, 6], 5))
print(merge([1, 2, 3, 5, 0, 0, 0, 0, 0, 0], 4, [-1, 0, 2, 4, 5, 6], 6))
