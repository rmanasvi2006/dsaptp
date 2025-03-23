def findDisappearedNumbersOptimal(nums):
    num_set = set(nums)
    return [i for i in range(1, len(nums) + 1) if i not in num_set]

nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbersOptimal(nums))
