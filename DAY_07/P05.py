# gold robber
# constraint: robber cannot rob consecutive houses
# return max rob value

def recur(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    ans1 = nums[0] + recur(nums[2:])
    ans2 = nums[1] + recur(nums[3:])
    return max(ans1, ans2)

nums = list(map(int, input().split()))
print(recur(nums))

