def containsDuplicateOptimal(nums):
    return len(set(nums)) < len(nums)

nums = [1, 2, 3, 4, 1]
print(containsDuplicateOptimal(nums))  
