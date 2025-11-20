# deletation of given position
arr = [1,2,3,4,5]
pos = 2
for i in range(pos - 1 , len(arr) - 1):
    arr[i] = arr[i + 1]

n = len(arr) - 1
for i in range(n):
    print(arr[i], end=" ")
print()
