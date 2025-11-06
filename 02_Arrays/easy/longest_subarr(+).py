def longest_subarray(arr, k):
    left = 0
    right = 0
    curr_sum = 0
    max_len = 0

    while right < len(arr):
        curr_sum += 1

        while curr_sum > k:
            curr_sum -= arr[left]

        if curr_sum == k:
            max_len = max(max_len , right - left + 1)
    
    return max_len