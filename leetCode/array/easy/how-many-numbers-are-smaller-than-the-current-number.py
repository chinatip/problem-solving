class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result = []
        numDic = {}

        for n in nums:
            if n not in numDic:
                numDic[n] = 1
            else:
                numDic[n] += 1

        numKeys = list(numDic.keys())
        for i in range(len(nums)):
            count = 0
            for n in numKeys:
                if nums[i] > n:
                    count += numDic[n]
            result += [count]

        return result
        