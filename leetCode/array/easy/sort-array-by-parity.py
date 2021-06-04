class Solution(object):
    def sortArrayByParity(self, nums):
        evenArr = []
        oddArr = []
        for val in nums:
            if val % 2 == 0:
                evenArr += [val]
            else:
                oddArr += [val]
        
        return evenArr + oddArr