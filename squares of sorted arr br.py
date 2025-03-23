def sortedSquaresBruteForce(nums):
    return sorted([x * x for x in nums])

nums = [-4, -1, 0, 3, 10]
print(sortedSquaresBruteForce(nums))
