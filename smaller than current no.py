def smallerNumbersThanCurrentOptimal(nums):
    sorted_nums = sorted(nums)
    num_map = {num: i for i, num in enumerate(sorted_nums)}
    return [num_map[num] for num in nums]

nums = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrentOptimal(nums))
