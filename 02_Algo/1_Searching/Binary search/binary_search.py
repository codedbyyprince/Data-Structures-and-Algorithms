# easy

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

arr = [1,3,5,7,9]

print(binary_search(arr , 7))

#  0   1   2   3   4   5   6   7   8
# [2,  5,  8, 12, 16, 23, 38, 45, 56]