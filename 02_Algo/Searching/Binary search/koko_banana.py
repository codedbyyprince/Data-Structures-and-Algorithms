# medium

# Koko eating bananas
from math import ceil

def minEatingspeed(piles, h):
    low = 1
    high = max(piles)
    score = 0 
    while low <= high:
        mid = (high + low) // 2
        for i in range(len(piles)):
            m = ceil(piles[i]/mid)
            score = score + m
        if score > h:
            low = mid + 1
        else:
            high = mid - 1
        return low