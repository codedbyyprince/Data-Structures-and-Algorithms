# medium 

# Search in rotated array 
def serach_in_rotated(arr, key ):
    n = len(arr)
    left = 0 
    right = n - 1 
    while left < right:
        mid = (left + right) // 2 
        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1 


#  0   1   2   3   4   5   6   7   8
# [23, 38, 45, 56, 2, 5, 8, 12, 16]
