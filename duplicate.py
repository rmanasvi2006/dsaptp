def containsDuplicateBruteForce(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

nums = [1, 2, 3, 4, 1]
print(containsDuplicateBruteForce(nums))  
