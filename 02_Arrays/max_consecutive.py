def max_consecutive(arr):
    n = len(arr)
    streaks = []
    count = 0 
    for i in range(n):  # start from 0 instead of 1
        if arr[i] == 1:
            count += 1
        else:
            if count > 0:
                streaks.append(count)
                count = 0
    # 👇 this is the key edge fix
    if count > 0:
        streaks.append(count)
        
    return max(streaks) if streaks else 0


arr = [1,1,0,0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1]
print(max_consecutive(arr))
