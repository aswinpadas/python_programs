# pylint: disable=missing-function-docstring
""" For fuure reference.
Given an array of integers nums and an integer target, return indices of the two numbers such
that they add up to target. You may assume that each input would have exactly one solution, and
you may not use the same element twice. You can return the answer in any order.

Algorithm that is less than O(n²) time complexity.
"""

# Solution: complexity O(n).


def get_indices(nums, target):
    processed_number_dict = dict()
    for index, num in enumerate(nums):
        if target - num in processed_number_dict:
            return [index, processed_number_dict[target - num]]
        else:
            processed_number_dict[num] = index


# Test cases

print(get_indices([1, 2, 3], 3))
print(get_indices([3, 2, 4], 6))
print(get_indices([2, 7, 11, 15], 9))
print(
    get_indices(
        [12, 15, 18, 21, 24, -27, 42, 45, 48, 57, 60, 72, -75, 96, 99, -102],
        -60))
print(
    get_indices(
        [12, 15, 18, 21, 24, -27, 42, 45, 48, 57, 60, 72, -75, 96, 99, -102],
        -50))
