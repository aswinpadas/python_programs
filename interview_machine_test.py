def get_indices(nums, target):
    for i in range(0, length := len(nums)):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return ([i, j])


# testcases

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
