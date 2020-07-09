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
    tree_root_index = int(len(arr)/2)
    print(tree_root_index)
    if arr[tree_root_index] == target:
        print("Target:", target)
        print("Tree root", arr[tree_root_index])
        print("They are equal why is this not returning?")
        return tree_root_index

    # Is the target bigger than the root?
    if target > arr[tree_root_index]:
        # Then search only the right side of the tree
        arr = arr[tree_root_index:]
        print(arr)
        binary_search(arr, target)

    elif target < arr[tree_root_index]:
        arr = arr[:tree_root_index + 1]
        binary_search(arr, target)

    return -1  # not found

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr1, 0))
