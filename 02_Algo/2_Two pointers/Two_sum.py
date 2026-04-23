# medium 

def Two_sum(nums , target):
    left = nums[0]
    right = len(nums) - 1

    while left < right:
        sums = nums[left] + nums[right]

        if sums == target:
            return [left + 1, right + 1]
        elif sums < target:
            left += 1
        else:
            right -= 1
