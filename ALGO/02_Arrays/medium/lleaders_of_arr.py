def leaders_of_arr(arr):
    n = len(arr)
    leaders = []
    for i in range(n):
        leader = True
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                leader = False
                break
        if leader:
            leaders.append(arr[i])
    return leaders


def leader_v2(arr):
    leader = []
    n = len(arr)

    max_lead = arr[-1]              
    leader.append(max_lead)         

    for i in range(n-2, -1, -1):    
        if arr[i] > max_lead:       
            max_lead = arr[i]       
            leader.append(arr[i])   

    leader.reverse()                
    return leader


arr =  [1, 2, 5, 3, 1, 2]
print(leaders_of_arr(arr))
print(leader_v2(arr))