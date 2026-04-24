# medium

from collections import Counter

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    s1_count = Counter(s1)      
    window_count = Counter()   

    left = 0
    right = 0

    while right < len(s2):
        # 1. add current character to window
        window_count[s2[right]] += 1

        # 2. keep window size = len(s1)
        if (right - left + 1) > len(s1):
            window_count[s2[left]] -= 1
            if window_count[s2[left]] == 0:
                del window_count[s2[left]]
            left += 1

        # 3. check match
        if window_count == s1_count:
            return True

        right += 1

    return False