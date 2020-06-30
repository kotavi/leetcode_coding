"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
    Input: [-4,-1,0,3,10]
    Output: [0,1,9,16,100]

Example 2:
    Input: [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

Note:
    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A is sorted in non-decreasing order.
"""


def sorted_squares_naive(lst):
    """
    Time Complexity: O(N*logN), where N is the length of A.
    Space Complexity: O(N).
    """
    return sorted([x*x for x in lst])


print(sorted_squares_naive([]))
print(sorted_squares_naive([12]))
print(sorted_squares_naive([-7, -3, 2, 3, 11]))
print(sorted_squares_naive([-4, -1, 0, 3, 10]))
print(sorted_squares_naive([-12, -10, -8, -6, -5, -4, -3, -2, -1]))


def sorted_squares(lst):
    """
    Two pointers approach

    Time Complexity: O(N), where N is the length of A.
    Space Complexity: O(N).
    """
    start = 0
    end = len(lst) - 1
    res_lst = [None for _ in range(len(lst))]
    i = len(lst) - 1
    while start <= end:
        if lst[start] * lst[start] < lst[end] * lst[end]:
            res_lst[i] = lst[end] * lst[end]
            end -= 1
        else:
            res_lst[i] = lst[start] * lst[start]
            start += 1
        i -= 1
    return res_lst


print("-*-" * 20)
print(sorted_squares([]))
print(sorted_squares([12]))
print(sorted_squares([-7, -3, 2, 3, 11]))
print(sorted_squares([-4, -1, 0, 3, 10]))
print(sorted_squares([-12, -10, -8, -6, -5, -4, -3, -2, -1]))
