def missingAndDuplicate(arr):
    i = 0

    # Put the items at their correct places
    while i < len(arr):
        if arr[i] != arr[arr[i] - 1]:
            # Swap
            val = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = val
        else:
           i += 1

    # Now find duplicate and repeated in the array
    for i in range(len(arr)):
        # If at any index, element is not the correct one, then that element is duplicate and index + 1 is missing element
        if arr[i] != i + 1:
            print("Duplicate Number ->",arr[i])
            print("Missing Number ->", i + 1)
            break

arr = [2,3,1,5,1]
missingAndDuplicate(arr)