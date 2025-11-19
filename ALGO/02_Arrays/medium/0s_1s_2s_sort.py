def sort_0s(arr):
    right = len(arr) - 1
    left = 0
    mid = 0

    while mid <= right:
        if arr[mid] == 0:
            arr[left], arr[mid] = arr[mid], arr[left]
            mid += 1
            left += 1

        elif arr[mid] == 1:
            mid += 1

        else:  # arr[mid] == 2
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1  # ✅ you missed this

    return arr

arr = [0,1,0,1,0,1,2,0,1,0,2,1,2,1,0]
print(sort_0s(arr))
