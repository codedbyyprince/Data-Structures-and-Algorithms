def remove_duplicates(arr):
    n = len(arr)
    m = []
    for i in range(n):
        if arr[i] not in m:
            m.append(arr[i])
    return m

arr = [1,2,22,2,4,6,2,1]
print(remove_duplicates(arr))