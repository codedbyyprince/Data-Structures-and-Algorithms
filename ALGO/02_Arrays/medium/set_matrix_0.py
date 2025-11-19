def set_arr_0(arr):
    cols = len(arr[0])
    rows = len(arr)
    
    rows_to_zero = set()
    cols_to_zero = set()

    for r in range(rows):
        for c in range(cols):
            if arr[r][c] == 0:
                rows_to_zero.add(r)
                cols_to_zero.add(c)
    
    for r in rows_to_zero:
        for c in range(cols):
            arr[r][c] = 0

    # 3. Zero out all marked columns
    for c in cols_to_zero:
        for r in range(rows):
            arr[r][c] = 0

    return arr