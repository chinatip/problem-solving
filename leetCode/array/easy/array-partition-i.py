class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        pairSum = 0
        
        i = 0
        while i < len(nums):
            pairSum += min(nums[i], nums[i+1])
            i += 2
            
        return pairSum
            
        