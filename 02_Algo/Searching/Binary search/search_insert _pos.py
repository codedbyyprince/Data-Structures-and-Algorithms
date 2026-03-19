def search_insert_position(arr, key):
    n = len(arr)
    l = 0 
    h = n - 1 
    while l<= h:
        mid = (l+h) // 2
        if key == arr[mid]:
            return mid 
        elif key < arr[mid]:
            h = mid - 1
        else:
            l = mid + 1
    return l

arr = [-1,0,2,4,6,8]
key = 10
print(search_insert_position(arr , key))