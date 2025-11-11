def majority_element(arr):
    n = len(arr)
    half = n // 2
    hashmap = {}

    for num in arr:                 
        hashmap[num] = hashmap.get(num, 0) + 1 

        if hashmap[num] > half:
            return num

arr = [5,5,5,5,6,7,8]
print(majority_element(arr))