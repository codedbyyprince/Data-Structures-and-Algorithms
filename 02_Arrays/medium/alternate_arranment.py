def rearrangeArray(arr):
    postive = []
    negative = []
    rearranged = []
    for i in arr:
        if i > 0 :
            postive.append(i)
        else:
            negative.append(i)
    for i in range(len(postive)):
        rearranged.append(postive[i])
        rearranged.append(negative[i])
    return rearranged

# optimal code
def rearrangeArray_v2(arr):
    result = [0] * len(arr)
    pos_index = 0  # even indexes
    neg_index = 1  # odd indexes
    
    for num in arr:
        if num > 0:
            result[pos_index] = num
            pos_index += 2
        else:
            result[neg_index] = num
            neg_index += 2
            
    return result


arr = [-1, 2, 4, 6, 7, -34, -2, -9]
print(rearrangeArray(arr))
print(rearrangeArray_v2(arr))