class Solution(object):
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result += [nums[i], nums[i + n]]
            
        return result
        