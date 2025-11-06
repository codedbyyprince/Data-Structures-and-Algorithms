def check_if_sorted(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            print(False)    
    print(True)

    
arr1 = [1,2,3,4,5,6,7,8]
arr2 = [1,3,4,6,7,8,9,4]
check_if_sorted(arr1)
check_if_sorted(arr2)