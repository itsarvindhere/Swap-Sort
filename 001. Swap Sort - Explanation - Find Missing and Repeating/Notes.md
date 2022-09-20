# WHEN NOT TO USE SWAP SORT?

If we are given a read-only array, then we cannot use Swap Sort. Beacuse in swap sort, we modify the original array. In this case we would have to go back to the previous two methods i.e., either using a map or maths.

# SWAP SORT

An ideal array from 1 to 5 will be like [2,3,1,5,4]

If we sort it, the array will be like 

    Index:  0  1  2  3  4
    Array   1  2  3  4  5

So as we can see, if the index is i, then element at that index is i + 1

Lets take an array -> [2,3,1,5,1]

If somehow, we can move elements to their indices correctly, such that each element is present at index = (element - 1) then we will get something like 

            [1,2,3, _ ,5]

Since there is no 4, that means at its place, we can put the element that appears twice. 

So our array becomes - 

            [1,2,3,1,5]

And once we convert the original array to an array like this, we can easily figure out what is the duplicate number and what is the missing number. Because now, all we need to do is traverse this array and at each index make sure it has index + 1 element. 

If any index does not have index + 1 element that means, the element present at that index is the duplicate element and the (index + 1) is the missing element.


    Index:  0  1  2  3  4
    Array   1  2  3  1  5

    At index 0, we have 0 + 1 = 1
    At index 1, we have 1 + 1 = 2 
    At index 2, we have 2 + 1 = 3
    At index 3, we have 3 + 1 = 4 ? NO! This means 4 is missing
    At index 3, we instead have 1. So, 1 is duplicate.
    At index 4, we have 4 + 1 = 5

    Hence, duplicate = 1 and missing = 4


So, the basic idea of SWAP SORT is to convert the given array in a useful array so that we can then find the duplicate or missing.

# SWAP SORT - ALGORITHM


    Index:  0  1  2  3  4
    Array   2  3  1  5  1


For every element at an index, we need to check if it is at its correct place or not. If not, then move it to its correct place by swapping the number at that place.

    Index:  0  1  2  3  4
    Array   2  3  1  5  1

At index = 0, we have 2. But 2 should be at (2 - 1) index. So, 2 should be at index = 1. This means, we need to swap element at index 1 with element at index 0
    
    Index:  0  1  2  3  4
    Array   3  2  1  5  1

Now we again check. 

AT index = 0, we have 3. But 3 should be at (3-1) i.e., index = 2

So, swap 3 with 1 which is at index = 2 currently

    Index:  0  1  2  3  4
    Array   1  2  3  5  1

Now we see that 1 is at index = 0 and it is at correct index.So we move to next element. Same for 2. It is at correct index.Same for 3 as it is at correct index.

Now, at index = 3, we have 5  But 5 should be at index = 4 so swap.

    Index:  0  1  2  3  4
    Array   1  2  3  1  5


Now, at index = 3, we have 1. But 1 should be at index = 0. But already at 0th index there is 1. This means, 1 is duplicate.

So to check if current element is duplicate check if 

        arr[i] == arr[arr[i] - 1]

And similarly, 
        
        Missing number = i + 1 => 3 + 1 => 4



# SWAP SORT - STEPS

There are two steps to solve the problem of finding missing and duplicate in an array.

    1. First Reorder the array such that each element is at its correct place (except the missing and duplicate)
    2. Once we get the array with each element at correct place, now check for repeated and missing.

So only if 1 is done properly, we can find the missing and duplicate element in the array.
