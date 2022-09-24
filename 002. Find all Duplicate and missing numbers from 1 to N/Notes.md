If there are multiple missing and duplicate numbers in the given array, then can we use Swap Sort method for that too?

In other words, is Swap Sort method scalable?


    e.g. nums = [2,3,1,8,2,3,5,1]

Here, length = 8 so the numbers in nums are from 1 to 8


SO as we do in swap sort, we will first reorder the array such that each index (except for those where element are missing)  has correct number. 

So for that, what we do is, for each index, see what element is there, and if that is not the correct element, move it to its correct plcae.


For any index i, if element is nums[i] then its correct place is nums[nums[i] - 1]


e.g. if index = 0 and element at that index is 2. That is not its correct place.

Correct place of 2 => nums[2 - 1] => nums[1] 

So, we will swap the number at nums[1] with 2 that is currently at nums[0] and this is how we will place each number in correct place.