def longest_subarray(arr, k):
    curr = 0 
    max_length = 0 
    prefix = {}

    for i in arr:
        curr = arr[i]
        if curr == k:
            max_length += 1
        if (curr - k) in prefix:
            length = i - prefix[curr - k]
            max_length = max(max_length , length)
        if curr not in prefix:
             prefix[curr] = i
    return max_length