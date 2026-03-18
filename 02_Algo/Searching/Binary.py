#  binary search

def binary_search(arr, key):
    l = 0
    h = len(arr) - 1

    while l <= h:
        mid = (l + h) // 2

        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            h = mid - 1
        else:
            l = mid + 1

    return -1