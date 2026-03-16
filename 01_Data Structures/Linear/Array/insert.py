# insertion at the beginning
arr = [2,3,4,5,0]
ele = 1
for i in range(len(arr) - 2, -1, -1):
    arr[i + 1] = arr[i]
arr[0] = ele
print("After insertion at beginning:", arr)

# insertion at given point
arr = [1,2,4,5,0]
ele = 3
pos = 4

for i in range(len(arr) - 2, pos - 2, -1):
    arr[i + 1] = arr[i]
arr[pos - 1] = ele
print("After insertion at given position:", arr)

# insertion at the end
arr = [1,2,3,4,0]
ele = 5
arr[len(arr) - 1] = ele
print("After insertion at the end:", arr)