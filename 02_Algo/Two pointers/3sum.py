# medium

def three_sum(nums):
    l = len(nums)
    nums.sort()
    triplets = []

    for i in range(l):
        x = nums[i]
        left = i + 1
        right = l - 1

        while left < right:
            sums = nums[left] + nums[right]

            if sums == -x:
                triplets.append([x, nums[left], nums[right]])
                left += 1
                right -= 1

            elif sums < -x:
                left += 1

            else:
                right -= 1

    return triplets