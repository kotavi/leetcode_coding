"""
Given a fixed length array arr of integers, duplicate each occurrence of zero,
shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.

Example 1:
    Input: [1,0,2,3,0,4,5,0]
    Output: null
    Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:
    Input: [1,2,3]
    Output: null
    Explanation: After calling your function, the input array is modified to: [1,2,3]

Note:
    1 <= arr.length <= 10000
    0 <= arr[i] <= 9
"""


def duplicate_zeros_naive(arr):
    """
    Approach:
    - loop through the input array;
    - if the current element is equal to 0:
        - insert another 0 to the right,
        - remove the last element from the array,
        - increase the index by one.
    - increase the index by one.
    """
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i+1, 0)
            arr.pop()
            i += 1
        i += 1
    return arr


print(duplicate_zeros_naive.__doc__)
print(duplicate_zeros_naive([1, 2, 3, 4, 5]))
print(duplicate_zeros_naive([1, 2, 3, 4, 5, 0]))
print(duplicate_zeros_naive([1, 0, 2, 3, 0, 4, 5, 0]))
print(duplicate_zeros_naive([0, 2, 3, 0, 4, 5, 0]))


def duplicate_zeros(arr):
    """
    Approach:
    -
    :param arr:
    :return:
    """
    n = len(arr)
    zeros = arr.count(0)
    curr_index = len(arr) - 1
    if not zeros:
        return arr
    while curr_index >= 0:
        if curr_index + zeros < n:
            arr[curr_index + zeros] = arr[curr_index]
        if arr[curr_index] == 0:
            zeros -= 1
            if curr_index + zeros < n:
                arr[curr_index + zeros] = 0
        curr_index -= 1
    return arr


print("-*-" * 20)
print(duplicate_zeros([1, 2, 3, 4, 5]))
print(duplicate_zeros([1, 2, 3, 4, 5, 0]))
print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))
print(duplicate_zeros([0, 2, 3, 0, 4, 5, 0]))

assert duplicate_zeros_naive([1, 2, 3, 4, 5]) == duplicate_zeros([1, 2, 3, 4, 5])
assert duplicate_zeros_naive([1, 0, 2, 3, 0, 4, 5, 0]) == duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])
assert duplicate_zeros_naive([0, 1, 2, 3, 4, 0, 5]) == duplicate_zeros([0, 1, 2, 3, 4, 0, 5])
assert duplicate_zeros_naive([1, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5]) == duplicate_zeros([1, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5])

