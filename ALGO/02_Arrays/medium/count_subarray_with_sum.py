def count_subarray_with_sum(arr, k):
    n = len(arr)
    count = 0

    for i in range(n):
        curr_sum = 0  
        
        for j in range(i, n):
            curr_sum += arr[j]

            if curr_sum == k:    
                count += 1

    return count
