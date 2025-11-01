def union_2(arr1, arr2):
    new = []
    
    for i in range(len(arr1)):
        new.append(arr1[i])
    
    for i in range(len(arr2)):
        new.append(arr2[i])
    n = len(new)
    
    new2 = []
    for i in range(n):
        if new[i] not in new2:
            new2.append(new[i])
    n2 = len(new2)
    for i in range(n2-1):
        mini = i
        for j in range(i+1,n2):
            if new2[j] < new2[mini]:
                mini = j
        new2[i] , new2[mini] = new2[mini], new2[i]
    return new2

arr1 = [1,23,54,7,2]
arr2 = [1,23,2,3,5,6,21]
print(union_2(arr1, arr2))