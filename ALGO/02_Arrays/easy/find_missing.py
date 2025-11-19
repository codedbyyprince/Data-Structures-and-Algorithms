def find(arr):
    m = []
    missing = []
    for i in range(arr[0], arr[-1] + 1):
        m.append(i)
    for i in m:
        if i not in arr:
            missing.append(i)
    
    return missing

arr = [1,3,4,5,6,7,9]
print(find(arr))