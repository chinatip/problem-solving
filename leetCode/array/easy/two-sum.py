class Solution(object):
    def twoSum(self, nums, target):
        numDic = {}
        for i in reversed(range(len(nums))):
            current = nums[i]
            targetPair = target - current
            if targetPair in numDic:
                return [i, numDic[targetPair]]
            if nums[i] not in numDic:
                numDic[current] = i
        return []
        