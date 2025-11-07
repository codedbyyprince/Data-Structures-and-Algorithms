def majority_element(arr):
    candidate = None
    votes = 0

    for num in arr:
        if votes == 0:
            candidate = num
        if num == candidate:
            votes += 1
        else:
            votes -= 1

    return candidate
