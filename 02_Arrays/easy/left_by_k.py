def rotate_left_by_k(arr,k):
    n = len(arr)
    m = arr[0]
    for _ in range(k):
        m = arr[0]
        for i in range(1, n):
            arr[i-1] = arr[i]
        arr[-1] = m
    return arr


arr = [1,2,3,4,5,6,7,8]
print(rotate_left_by_k(arr , 2))
