def move_0_to_left(arr):
    n = len(arr)
    pos = 0
    for i in range(1,n):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
    for i in range(pos, n):
        arr[i] = 0
    return arr
arr = [0, 1, 4, 0, 5, 2]
print(move_0_to_left(arr))