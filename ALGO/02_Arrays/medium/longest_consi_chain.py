def longest_consecutive_sequence(arr):
    longest = 0 
    s = set(arr)
    for i in s:
        if arr[i] - 1 not in arr:
            length = 1
            next = i + 1 
            while next in s:
                length += 1
                next  += 1
                longest = max(longest, length)

    return longest

