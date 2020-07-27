from math import floor
def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # Find the middle number for the root of the tree
    start = 0
    end = len(arr) - 1
    unfound = True
    while unfound and end >= start:

        mid = (start + end) // 2

        if arr[mid] == target:
            unfound = False
            return mid

        elif target > arr[mid]:
            start = mid + 1
        
        elif target < arr[mid]:
            print(start)
            end = mid -1 

    return -1  # not found

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr1, -6))
