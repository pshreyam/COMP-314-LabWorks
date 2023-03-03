from decorators import timer


@timer
def insertion_sort(array):
    """Return the array sorted using insertion sort."""
    # Get the length of the array
    n = len(array)
    # Loop through each item of the array
    for j in range(1, n):
        # Set the jth element as a key
        key = array[j]
        i = j - 1
        # Push the element at the jth position to its current position
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key


@timer
def merge_sort(array, p, r):
    """Sort the given array using divide and conquer."""
    if p < r:
        q = (p + r) // 2
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)


def merge(array, p, q, r):
    """Merge sub-arrays."""
    left_arr = array[p:q + 1]
    right_arr = array[q + 1:r + 1]
    i = j = 0

    for k in range(p, r + 1):
        if left_arr[i] <= right_arr[j]:
            array[k] = left_arr[i]
            i = i + 1
            if i >= len(left_arr) and j < len(right_arr):
                for l in range(k + 1, r + 1):
                    array[l] = right_arr[j]
                    j = j + 1
                break
        else:
            array[k] = right_arr[j]
            j = j + 1
            if j >= len(right_arr) and i < len(left_arr):
                for l in range(k + 1, r + 1):
                    array[l] = left_arr[i]
                    i = i + 1
                break
