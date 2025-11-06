def search(arr, m):
    for i in range(len(arr)):
        if arr[i] == m:
            return i
    return -1

arr = [1,2,3,4,5,6,9,10]
print(search(arr, 10))