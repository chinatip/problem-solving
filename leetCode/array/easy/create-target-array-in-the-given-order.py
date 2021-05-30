class Solution(object):
    def createTargetArray(self, nums, index):
        result = []
        
        for i in range(len(index)):
            result = result[:index[i]] + [nums[i]] + result[index[i]:]
            #result.insert(index[i], nums[i])
        return result