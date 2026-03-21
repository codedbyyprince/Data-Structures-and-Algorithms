# medium

# Find minimum in rotated sorted array
def min_in_arr(arr):
    n = len(arr)
    left = 0 
    right = n -1 
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid 
    return arr[left]


#  0   1   2   3   4   5   6   7   8
# [23, 38, 45, 56, 2, 5, 8, 12, 16]
