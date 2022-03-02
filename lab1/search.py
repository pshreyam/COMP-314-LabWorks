from decorators import timer


@timer
def linear_search(arr, key):
    """Search for a key in array of items linearly and return the index if the key is present in the array."""
    for i, value in enumerate(arr):
        if key == value:
            return i
    return -1


@timer
def binary_search(arr, key):
    """Search for a key by dividing the problem into two subproblems and return the index if the key is present in the array."""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1
