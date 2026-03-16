arr = [1,2,3,4,5,6,75,232,2]
print('Input the num u want to serach ')
user_input = int(input())

for i in arr:
    if i == user_input:
        print(f'{i} is found at index {arr.index(i)}')
        break
else:
    print('Not found')
