class Solution(object):
    def decompressRLElist(self, nums):
        result = []
        i = 0
        while i < len(nums):
            result += [nums[i + 1]] * nums[i]
            i += 2
            
        return result 
        