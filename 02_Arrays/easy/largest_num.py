def largest_num(arr):
    largest = arr[0]
    for i in range(1 ,len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

arr =  [3, 3, 6, 1]
print(largest_num(arr)) 