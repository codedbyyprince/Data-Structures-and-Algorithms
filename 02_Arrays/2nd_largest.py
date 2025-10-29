def second_largest(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    last = arr[-1]
    for i in range(n - 2, -1, -1):
        if arr[i] != last:
            print(arr[i])
            return
    print("No second largest element")

arr = [8,8,8,8,8,8,8,8,7,6,5]
second_largest(arr)
