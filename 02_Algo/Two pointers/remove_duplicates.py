# easy 

def remove_duplicates_from_sorted_arr(arr):
    if len(arr) == 0:
        return 0 
    
    write = 1 

    for scan in range(1, len(arr)):
        if arr[scan] != arr[scan - 1]:
            arr[write] = arr[scan]
            write += 1 
         
    return write
