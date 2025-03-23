def sortedSquaresOptimal(nums):
    result = [0] * len(nums)
    left, right, pos = 0, len(nums) - 1, len(nums) - 1
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] ** 2
            left += 1
        else:
            result[pos] = nums[right] ** 2
            right -= 1
        pos -= 1
    return result

nums = [-4, -1, 0, 3, 10]
print(sortedSquaresOptimal(nums))
