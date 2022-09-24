def missingAndDuplicate(nums):
    missing = []
    duplicate = []

    # First place each number at its correct place
    i = 0
    while i < len(nums):
        if nums[i] != nums[nums[i] - 1]:
            #Swap
            val = nums[nums[i] - 1]
            nums[nums[i] - 1] = nums[i]
            nums[i] = val
        else: 
            i += 1

    # Now find missing and duplicates
    for i, num in enumerate(nums):
        if num != i + 1:
            missing.append(i + 1)
            duplicate.append(num)


    return missing + duplicate


nums = [2,3,1,8,2,3,5,1]
print("Given Array is -> ", nums)


missing, duplicate = missingAndDuplicate(nums)
print("Missing Numbers ->", missing)
print("Duplicate Numbers ->", duplicate)
