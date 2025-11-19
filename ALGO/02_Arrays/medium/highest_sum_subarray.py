def maxsum_subarray(arr):
    n = len(arr)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    return max_sum

# opitmal code 
def v2_maxsum_subarray(arr):
    current = arr[0]
    best = arr[0]
    for i in range(len(arr)):
        current = max(arr[i] + current + arr[i])
        best = max(best, current)
    return best