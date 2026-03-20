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