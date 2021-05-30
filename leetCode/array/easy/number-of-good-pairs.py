class Solution(object):
    def numIdenticalPairs(self, nums):
        numPair = 0
        for i in range(len(nums) - 1):
            j = len(nums) -1

            while j > i:
                if nums[i] == nums[j]:
                    numPair += 1
                j -= 1
        return numPair
        