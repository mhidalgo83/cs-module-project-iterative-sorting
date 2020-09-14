def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return arr.index(arr[i])
    
    return -1
    


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    left = 0
    right = len(arr) - 1

    while left <= right:
        midpoint = (right + left) // 2
        if arr[midpoint] == target:
            return arr.index(target)
        elif arr[midpoint] > target:
            right = midpoint - 1
        elif arr[midpoint] < target:
            left = midpoint + 1
    
    return -1  # not found
