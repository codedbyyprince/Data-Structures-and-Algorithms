def two_sum(arr, k):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                return [i, j]

def two_sum_v2(nums, target):
    hashmap = {}  # stores {number: index}

    for i, num in enumerate(nums):
        need = target - num
        if need in hashmap:
            return [hashmap[need], i]  # found the pair
        hashmap[num] = i  

arr = [1,6,3,3,78,6,1]
k = 7

print(two_sum(arr, k))
