# transverse array
arr = [1,2,3,4,5]
for i in arr:
    print(i, end=' ')
print()

# reverse transverse array
for i in range(len(arr)-1, -1 , -1):
    print(arr[i], end=' ')
print()

# while loop
while i < len(arr):
    print(arr[i], end='')
print()

# use cases 
# 1. searching an element 
target = 3
for i in range(len(arr)):
    if arr[i] == target:
        print(f"element {target} found at index {i}")
        break

arr = [10, 20, 30, 40, 50]

#2. Modifying elements using traversal
    arr[i] += 5

# Print modified array
print("Modified array:", end=' ')
for num in arr:
    print(num, end=' ')
print()