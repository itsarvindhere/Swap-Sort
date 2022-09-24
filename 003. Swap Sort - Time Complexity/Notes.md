Is the time complexity of this algorithm exactly O(n)?

It is not exactly N but slightly higher than N.

Below is the code for placing each number at its correct place - 

    i = 0
    while i < len(nums):
        if nums[i] != nums[nums[i] - 1]:
            #Swap
            val = nums[nums[i] - 1]
            nums[nums[i] - 1] = nums[i]
            nums[i] = val
        else: 
            i += 1

Here, we we can see, i is only incremented if the number is already at its correct place. Otherwise, we keep swapping the number at ith index.

So now the question is, what is the maximum number of swaps we can do at one index?

If at an index, the maximum swaps we can do is n itself, then in worst case, the above code wil run n*n times which is O(n^2). But lets see what is the maximum swaps that can take place at an index.

# WORST CASE SCENARIO

It is worth noticing that, for each index, the swap that we do is not a random swap. This means, if at any index we have wrong element, then we take that element and put it in its corect place. So even if current index may not get the correct element, the element that we moved to a different index is guaranteed to be at its correct place.


    e.g. [2, 3, 1, 3]

    At index = 0, we have 2. Since the correct place of 2 is index = 1 so we swap index 0 and index 1

    [3,2,1,3]

    Now, index 0 is still not having the correct element. But take a look at index 1. It now has the correct element at its place which is 2.

    This means, we will never have to swap the index 1 because it is now already having a correct element.


What this means is, in each swap, there are two cases -

    1. Either one index will get a correct element
    2. Both indices get correct elements

So, there is no case when a swap results in no indices getting a correct element


Lets take this array to understand the worst case -

    [5, 1, 2, 3, 4, 1]

Lets see at each index, how many swaps we have to do until we get a correct element at that index.


At index = 0, we have 5. Because it is not correct element, we move 5 to its correct index which is 4.

    One Swap -> [4,1,2,3,5,1]

Again, at index = 0, we have 4. It is not correct element so move it to its correct index which is index 3.

    Two swaps -> [3,1,2,4,5,1]

Again the same.

    Three Swaps -> [2,1,3,4,5,1]

Again the same

    Four swaps -> [1,2,3,4,5,1]

And now, index 0 has correct element. So, we did 4 swaps.

Lets move to index = 1. It has element = 2 which is already at its correct place. No Swaps.

Move to index = 2, element is 3 so it is alread at its correct place. So No swaps.

Move to index = 3. Element is 4 and it is already at correct place so no swaps.

Move to index = 4. Element is 5 and it is already at correct place so no swaps

And finally, index = 5. Element is 1 and as we see, 1 should be at index = 0. Since index = 0 has 1 already, that means no swaps here as well.


SO in total, we had to do 4 swaps to place all the numbers in their correct place.


Hence, the worst case is when for one index, we swap all the indices.

So, for an array of length n, we can do at most (n-1) swaps at first index. And in that case, all the indices after first index will already be having correct elements after (n-1) swaps.

So in the worst case, the above code will run in (n-1) + (n-1) or 2n-2 or Order of n


because if index 0 does n - 1 swaps that means, for index 0, there are (n-1) iterations. 

But if that's the case, then rest of elements won't be swapped so for them, we just do i++ which means for the rest (n-1) elements, no swaps hence O(1) time

So total complexity - 

(1 * (n-1)) + ((n-1) * 1)) => (n-1) + (n-1) => 2n - 2 ~ O(n)

And the other piece of code runs exactly n times so for that complexity is O(n) only.

Hence, for this algorithm, the time complexity is O(n)
And as we used no space, Space Complexity is O(1)