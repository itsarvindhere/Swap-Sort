# PROBLEM STATEMENT

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Range of numbers is from -2^31 to 2^31 - 1

# HOW TO USE SWAP SORT IN THIS CASE?

It is not given that we have numbers from 1 to n only. Then how can we use swap sort?

We have to find the smallest missing positive number. That means, we only care about the positive numbers here i.e., greater than 0

And the smallest missing number also means the first missing number because index starts from 0 and as we know, ideally, 0th index should have element = 0 + 1 = 1 which is the smallest positive number.

So, what we can do is we manually pick the range 1 to n where n is the length of given array and then place each element at its correct place.


    e.g. nums = [3,4,-1,1]

So here, n = 4 which means ideally, all numbers from 1 to 4 should be in this array. Lets apply swap sort on this array. And as we care only about positives, we will only care about 1 to n numbers.

    at index = 0, we have 3. is 3 > 0 and <= n? YES. SO it can be considered. 

    It 3 at its correct place? NO. Its correct place is index 2.

    So swap element at index 2 with 3. 

    [-1,4,3,1]

    Now at index = 0, we have a negative number so we ignore it and move ahead.

    At index = 1, we have 4. It should be at index = 3. SO swap

    [-1,1,3,4]

    Again at index = 1, we have 1. But 1 should be at index = 0. So Swap.

    [1,-1,3,4]

    And since now we have a negative number at index = 1, ignore it.


    At index = 2, we already have correct number i.e, 3

    AT index = 3 we already have correct number i.e., 4


So finally, our array becomes [1,-1,3,4]

ANd now, we do the second part of Swap Sort algorithm, which is to find the missing number. If at index = i, we do not have i + 1, that means i + 1 is the missing number. And because we are asked to find the first positive missing number, as soon as we find a missing number, that will be the first/smallest so we can return.


So, in [1,-1,3,4] we will see that at index = 1, we should have 2 but instead there is -1. This means 2 is missing. So return 2.

# SPECIAL CASES

There will be cases where we have arrays like - 

    [1]

And in this case, smallest positive missing number is 2. That's because as we know, range is from -2^31 to 2^31 - 1. So if 1 is there, then the next smallest number is 2 which is missing.


But our swap sort algorithm won't be able to find it because we run the loop only till length of the array which in this case is 1.

So, if we did not get a missing number from swap sort, that simply means the missing number is the next number i.e., (length + 1)