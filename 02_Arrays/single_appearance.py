def single_appearance(arr):
    count = {}
    for n in arr:
        count[n] = count.get(n, 0) + 1
    for n in count:
        if count[n] == 1:
            return n


arr = [1,3,5,7,9,3]
print(single_appearance(arr))