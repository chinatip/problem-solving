class Solution(object):
    def sumOfUnique(self, nums):
        self.numsCount = {}
        for val in nums:
            if val in self.numsCount:
                self.numsCount[val] += 1
            else:
                self.numsCount[val] = 1
        
        self.sumUniq = 0
        for val in list(self.numsCount.keys()):
            self.sumUniq += val if self.numsCount[val] == 1 else 0
        
        return self.sumUniq
        