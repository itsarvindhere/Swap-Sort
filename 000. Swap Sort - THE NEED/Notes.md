# PROBLEM STATEMENT

Given an unsorted array of size N of positive integers. One number 'A' is missing and one number 'B' occurs twice in array. Find these two numbers.

Numbers in the array are from 1 to n

# EXAMPLE

Array = [1,3,3], N = 3

Here, since N = 3, that means array should have 1, 2 and 3
But here, "2" is missing. 
Also, "3" occurs twice. 

Hence, 

Duplicate Number = 3
Missing Number = 2

# 1. SOLVING THIS PROBLEM USING A MAP

One way to solve this problem is to use a Map to store the count of each number in the array.

    e.g. for [1,3,3]

    map = {1 : 1, 3 : 2}

And now, we can loop from 1 to N i.e., 1 to 3 and for each number, check if it is present in map or not. If yes, then check its count. If its count is 2, that means it is duplicate.

Similarly, if a number is not in map, then it is a missing number.

So this way, we can get the missing number and the duplicate number.

# THE PROBLEM WITH THIS APPROACH

The issue with this approach is the Space Complexity. That's because we are using a Map to store all the numbers in array. So space complexity becomes O(N)

What if we are asked to solve this problem in O(1) space? How to do that? 


# 2. SOLVING THIS PROBLEM USING MATHS

We want to find two numbers - missing and duplicate

and in maths, when there are two values to find, we have two equations. So lets try to find two such equations.

Since we are give numbers from 1 to N, what will the sum of 1 to N minus the sum of given array will give us?

e.g. [1,3,3]

    Sum from 1 to N => 1 + 2 + 3
    Sum of above array => 1 + 3 + 3

    (1 + 2 + 3) - (1 + 3 + 3) 
    1 + 2 + 3 - 1 - 3 - 3

So after numbers cancel out each other, we get

        2 - 3

Now just think about this. 

    2 is the missing number in [1,3,3]
    3 is the duplicate number in [1,3,3]

This means, 

    Sum (1 to N) - Sum(array) => missing number - duplicate number
    
    Since left side is constant, that means

    c1 = missing number - duplicate number ----- (1)

This is our first equation.

Now to find the second equation, lets find the sum of squares from 1 to N and sum of squares of elements of given array.

    Sum of squares from 1 to N => (1^2) + (2^2) + (3^2)
    Sum of squares of elements of array => (1^2) + (3^2) + (3^2)


If we substract these two -


    (1^2) + (2^2) + (3^2) - (1^2) - (3^2) - (3^2)
    
    After various +ve and -ve numbers cancel each out, we get

    (2^2) - (3^2)

    Which means (square of missing number) - (square of duplicate number)

So, dividing these,

    Sum of Square(1 to N) - Sum of square(array)     square(missing) - square(duplicate)
    ----------------------------------------     =   ----------------------------------
    Sum (1 to N) - Sum(array)                              missing - duplicate


The left side is something we can find out because all the values are known to us. To left side is some constant value.

This means, 

                square(missing) - square(duplicate)
        c2 =      --------------------------------
                     missing - duplicate


And as we know, a^2 - b^2 = (a + b)(a - b)

                (missing + duplicate) * (missing - duplicate)
        c2 =      --------------------------------------------
                            missing - duplicate

So finally, we get

        c2 = missing + duplicate ------ (2)


And this is our second equation


So, from (1) and (2), if we have - 

    c1 = missing - duplicate
    c2 = missing + duplicate

Adding both

    c1 + c2 = missing - duplicate + missing + duplicate
    c1 + c2 = 2 * (missing)
    missing number = (c1 + c2) /2 ------- (3)


So using this equation, we can find missing number. And once we find missing number, we can also find duplicate usign any of the equations above.

# THE PROBLEM WITH THIS APPROACH

There is too much calculation need to do to just figure out just one duplicate number and one missing number. If there were multiple missing and duplicate, it would've been so difficult to figure out equations for those. 


# SWAP SORT TO THE RESCUE

And now, we come to a very interesting approach for this problem using Swap sort.