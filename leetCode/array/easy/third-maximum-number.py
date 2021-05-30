class Solution(object):
    def thirdMax(self, nums):
        nums.sort()
        if len(nums) < 3:
            return nums[-1]
        count = 0
        last = nums[-1]
        for i in reversed(range(len(nums))):
            if last == nums[i]:
                last = nums[i]
                continue
            count += 1
            last = nums[i]
            
            if count == 2:
                return nums[i]
        return nums[-1]
        