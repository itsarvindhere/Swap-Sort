def firstMissingPositive(nums):
    n = len(nums)
        
    #First place each number at its correct place in range 1 to n
    i = 0
        
    while i < n:
        # Swap
        # Only for the range 1 to n
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i]= nums[i], nums[nums[i] - 1]
        else:
            i += 1
        
    # And now just find the first missing number. That would be the smallest
    for i,num in enumerate(nums):
        if num != i + 1: return i + 1
        
    # Otherwise the missing positive number is n + 1 (e,g, for testcases such as [1])
    return n + 1



nums = [7,8,9,11,12]
print("Given Array is ->", nums)
print("First Missing Positive Numbers is -> ",firstMissingPositive(nums))