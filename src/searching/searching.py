

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    # Your code here


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = arr[middle]
        if guess == target:
            return middle
        if target > guess:
            low = middle + 1

        else:
            high = middle - 1




    return -1  # not found
