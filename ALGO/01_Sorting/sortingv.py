import time

def selction_sort(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if arr[j]<arr[mini]:
                mini = j 
        arr[i], arr[mini] = arr[mini], arr[i]
    
    print(*arr)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] , arr[j]
    print(*arr)

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i -1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr [j]
        j -= 1
    arr[j+1] = key
    print(*arr)

# merge sort part 1
def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr)//2
    left =  merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
# merge sort part 2
def merge(left , right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i = i + 1
        else:
            merged.append(right[j])
            j = j + 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    n = len(arr) 
    right = []
    left = []
    equal = []
    pt = n // 2
    pivot = arr[pt]

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)

    return quick_sort(left) + equal + quick_sort(right)

# Test
arr = [1,5,5,874,54,798,4,7,8]    
print(quick_sort(arr))



arr = [ 1,4, 6, 2 ,2, 5, 7, 8 ,3 ]

# Time calculation for each sort
print("\nTime taken by each sorting algorithm:")
print("-" * 40)

# Selection Sort
start_time = time.time()
arr_copy = arr.copy()
print("Selection Sort:", end=" ")
selction_sort(arr_copy)
print(f"Time: {time.time() - start_time:.6f} seconds")

# Bubble Sort
start_time = time.time()
arr_copy = arr.copy()
print("Bubble Sort:", end=" ")
bubble_sort(arr_copy)
print(f"Time: {time.time() - start_time:.6f} seconds")

# Insertion Sort
start_time = time.time()
arr_copy = arr.copy()
print("Insertion Sort:", end=" ")
insertion_sort(arr_copy)
print(f"Time: {time.time() - start_time:.6f} seconds")

# Merge Sort
start_time = time.time()
arr_copy = arr.copy()
print("Merge Sort:", end=" ")
sorted_arr = merge_sort(arr_copy)
print(*sorted_arr)
print(f"Time: {time.time() - start_time:.6f} seconds")